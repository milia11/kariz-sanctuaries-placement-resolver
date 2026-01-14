import numpy as np
from scipy.optimize import linear_sum_assignment


class Sanctuaries:
    def __init__(self,
                 kou_bou=0,  # M攻防
                 bin_sho=0,  # M敏捷
                 sho_geki=0,  # M衝撃
                 katsu_ryoku=0,  # M活力
                 sei_ki=0,  # M生気
                 tai_ryoku=0,  # M耐力
                 bou_gyo=0,  # M防御
                 bou_gyo_mu_shi=0,  # M防御無視
                 kyo_ko=0,  # M強攻
                 kyo_ko_tei_ko=0,  # M強攻抵抗
                 kou_geki=0,  # M攻撃
                 ):
        self.kou_bou = kou_bou
        self.bin_sho = bin_sho
        self.sho_geki = sho_geki
        self.katsu_ryoku = katsu_ryoku
        self.sei_ki = sei_ki
        self.tai_ryoku = tai_ryoku
        self.bou_gyo = bou_gyo
        self.bou_gyo_mu_shi = bou_gyo_mu_shi
        self.kyo_ko = kyo_ko
        self.kyo_ko_tei_ko = kyo_ko_tei_ko
        self.kou_geki = kou_geki

    @property
    def score(self):
        # return sum(self.__dict__.values())
        # 攻撃専門
        return (
                self.kou_bou +
                self.bin_sho * (1 + 0.01) +
                self.sho_geki +
                self.bou_gyo_mu_shi*0.01 +
                self.kou_geki
            # +
            # self.tai_ryoku +
            # self.katsu_ryoku +
            # self.sei_ki * 2

        )


# データを辞書形式で定義（アイテム名を含む）
data = {
    "極盛マッシュの杖": [
        Sanctuaries(bin_sho=7275, sei_ki=7875),
        Sanctuaries(kou_bou=10125, kyo_ko_tei_ko=5850),
        Sanctuaries(tai_ryoku=7875, bou_gyo_mu_shi=2550),
        Sanctuaries(katsu_ryoku=8550, kyo_ko=2550),
        Sanctuaries(sho_geki=7275, bou_gyo=12450),
        Sanctuaries(kou_geki=2550, bou_gyo=12450),
        Sanctuaries(kou_bou=10125, sei_ki=7875),
        Sanctuaries(tai_ryoku=7875, bin_sho=7275),
        Sanctuaries(katsu_ryoku=8550, bou_gyo_mu_shi=2550),
        Sanctuaries(kyo_ko=2550, kyo_ko_tei_ko=5850),
    ],
    "アストラ王の鎧": [
        Sanctuaries(bin_sho=4800, sei_ki=8730),
        Sanctuaries(kou_bou=11205, kyo_ko_tei_ko=5850),
        Sanctuaries(tai_ryoku=8730, bou_gyo_mu_shi=6262),
        Sanctuaries(katsu_ryoku=8550, kyo_ko=2550),
        Sanctuaries(sho_geki=8355, bou_gyo=23142),
        Sanctuaries(kou_geki=2550, bou_gyo=23142),
        Sanctuaries(kou_bou=11205, sei_ki=8730),
        Sanctuaries(tai_ryoku=8730, bin_sho=4800),
        Sanctuaries(katsu_ryoku=8550, bou_gyo_mu_shi=6262),
        Sanctuaries(kyo_ko=2550, kyo_ko_tei_ko=5850),
    ],
    "ユピテル王の法環": [
        Sanctuaries(bin_sho=9075, sei_ki=5850),
        Sanctuaries(kou_bou=7650, kyo_ko_tei_ko=11682),
        Sanctuaries(tai_ryoku=9306, bou_gyo_mu_shi=2550),
        Sanctuaries(katsu_ryoku=12046, kyo_ko=7005),
        Sanctuaries(sho_geki=4800, bou_gyo=12450),
        Sanctuaries(kou_geki=15379, bou_gyo=12450),
        Sanctuaries(kou_bou=7650, sei_ki=5850),
        Sanctuaries(tai_ryoku=9306, bin_sho=9075),
        Sanctuaries(katsu_ryoku=12046, bou_gyo_mu_shi=2550),
        Sanctuaries(kyo_ko=7005, kyo_ko_tei_ko=11682),
    ],
    "エーギル王の戦矛": [
        Sanctuaries(bin_sho=4800, sei_ki=9648),
        Sanctuaries(kou_bou=7650, kyo_ko_tei_ko=5850),
        Sanctuaries(tai_ryoku=5850, bou_gyo_mu_shi=7450),
        Sanctuaries(katsu_ryoku=12348, kyo_ko=7450),
        Sanctuaries(sho_geki=9502, bou_gyo=26562),
        Sanctuaries(kou_geki=2550, bou_gyo=26562),
        Sanctuaries(kou_bou=7650, sei_ki=9648),
        Sanctuaries(tai_ryoku=5850, bin_sho=4800),
        Sanctuaries(katsu_ryoku=12348, bou_gyo_mu_shi=7450),
        Sanctuaries(kyo_ko=7450, kyo_ko_tei_ko=5850),
    ],
    "エーギル王の戦鎧": [
        Sanctuaries(bin_sho=4800, sei_ki=5850),
        Sanctuaries(kou_bou=13311, kyo_ko_tei_ko=13590),
        Sanctuaries(tai_ryoku=10440, bou_gyo_mu_shi=8472),
        Sanctuaries(katsu_ryoku=13140, kyo_ko=2550),
        Sanctuaries(sho_geki=4800, bou_gyo=12450),
        Sanctuaries(kou_geki=19560, bou_gyo=12450),
        Sanctuaries(kou_bou=13311, sei_ki=5850),
        Sanctuaries(tai_ryoku=10440, bin_sho=4800),
        Sanctuaries(katsu_ryoku=13140, bou_gyo_mu_shi=8472),
        Sanctuaries(kyo_ko=2550, kyo_ko_tei_ko=13590),
    ],
    "エーギル王の明灯": [
        Sanctuaries(bin_sho=11010, sei_ki=10890),
        Sanctuaries(kou_bou=7650, kyo_ko_tei_ko=5850),
        Sanctuaries(tai_ryoku=5850, bou_gyo_mu_shi=2550),
        Sanctuaries(katsu_ryoku=13590, kyo_ko=7005),
        Sanctuaries(sho_geki=11010, bou_gyo=31170),
        Sanctuaries(kou_geki=2550, bou_gyo=31170),
        Sanctuaries(kou_bou=7650, sei_ki=10890),
        Sanctuaries(tai_ryoku=5850, bin_sho=11010),
        Sanctuaries(katsu_ryoku=13590, bou_gyo_mu_shi=2550),
        Sanctuaries(kyo_ko=7005, kyo_ko_tei_ko=5850),
    ],
    "至上マッシュの扇": [
        Sanctuaries(bin_sho=11640, sei_ki=11385),
        Sanctuaries(kou_bou=14490, kyo_ko_tei_ko=15210),
        Sanctuaries(tai_ryoku=11385, bou_gyo_mu_shi=9705),
        Sanctuaries(katsu_ryoku=8550, kyo_ko=2550),
        Sanctuaries(sho_geki=4800, bou_gyo=12450),
        Sanctuaries(kou_geki=2550, bou_gyo=12450),
        Sanctuaries(kou_bou=14490, sei_ki=11385),
        Sanctuaries(tai_ryoku=11385, bin_sho=11640),
        Sanctuaries(katsu_ryoku=8550, bou_gyo_mu_shi=9705),
        Sanctuaries(kyo_ko=2550, kyo_ko_tei_ko=15210),
    ],
    "ラケシス王の天秤": [
        Sanctuaries(bin_sho=4800, sei_ki=5850),
        Sanctuaries(kou_bou=7650, kyo_ko_tei_ko=16132),
        Sanctuaries(tai_ryoku=5850, bou_gyo_mu_shi=10402),
        Sanctuaries(katsu_ryoku=14647, kyo_ko=10402),
        Sanctuaries(sho_geki=4800, bou_gyo=33037),
        Sanctuaries(kou_geki=21225, bou_gyo=33037),
        Sanctuaries(kou_bou=7650, sei_ki=5850),
        Sanctuaries(tai_ryoku=5850, bin_sho=4800),
        Sanctuaries(katsu_ryoku=14647, bou_gyo_mu_shi=10402),
        Sanctuaries(kyo_ko=10402, kyo_ko_tei_ko=16132),
    ],
    "エーギル王の貝笛": [
        Sanctuaries(bin_sho=11010, sei_ki=10890),
        Sanctuaries(kou_bou=7650, kyo_ko_tei_ko=5850),
        Sanctuaries(tai_ryoku=5850, bou_gyo_mu_shi=2550),
        Sanctuaries(katsu_ryoku=13590, kyo_ko=9052),
        Sanctuaries(sho_geki=11010, bou_gyo=31170),
        Sanctuaries(kou_geki=2550, bou_gyo=31170),
        Sanctuaries(kou_bou=7650, sei_ki=10890),
        Sanctuaries(tai_ryoku=5850, bin_sho=11010),
        Sanctuaries(katsu_ryoku=13590, bou_gyo_mu_shi=2550),
        Sanctuaries(kyo_ko=9052, kyo_ko_tei_ko=5850),
    ],
    "幻マッシュの薬缶": [
        Sanctuaries(bin_sho=13035, sei_ki=12532),
        Sanctuaries(kou_bou=15885, kyo_ko_tei_ko=18270),
        Sanctuaries(tai_ryoku=12532, bou_gyo_mu_shi=12045),
        Sanctuaries(katsu_ryoku=8550, kyo_ko=2550),
        Sanctuaries(sho_geki=4800, bou_gyo=12450),
        Sanctuaries(kou_geki=2550, bou_gyo=12450),
        Sanctuaries(kou_bou=15885, sei_ki=12532),
        Sanctuaries(tai_ryoku=12532, bin_sho=13035),
        Sanctuaries(katsu_ryoku=8550, bou_gyo_mu_shi=12045),
        Sanctuaries(kyo_ko=2550, kyo_ko_tei_ko=18270),
    ],
    # "ラケシス王の大剣": [  # Lv21
    #     Sanctuaries(bin_sho=3390, sei_ki=4200),
    #     Sanctuaries(kou_bou=5400, kyo_ko_tei_ko=14215),
    #     Sanctuaries(tai_ryoku=4200, bou_gyo_mu_shi=9108),
    #     Sanctuaries(katsu_ryoku=11535, kyo_ko=8446),
    #     Sanctuaries(sho_geki=3390, bou_gyo=29020),
    #     Sanctuaries(kou_geki=16164, bou_gyo=29020),
    #     Sanctuaries(kou_bou=5400, sei_ki=4200),
    #     Sanctuaries(tai_ryoku=4200, bin_sho=3390),
    #     Sanctuaries(katsu_ryoku=11535, bou_gyo_mu_shi=9108),
    #     Sanctuaries(kyo_ko=8446, kyo_ko_tei_ko=14215),
    # ],
}

# アイテム名のリストを作成（順序を保持）
item_names = list(data.keys())

# スコアの重み行列作成
weights = np.array([[item.score for item in data[name]] for name in item_names])

# n×n行列かどうかをチェック
rows, cols = weights.shape
if rows != cols:
    raise ValueError(f"weights行列は正方行列である必要があります。現在のサイズ: {rows}×{cols}")

max_value = np.max(weights)
cost_matrix = max_value - weights  # コスト行列（スコア最大化→最小化に変換）

# ハンガリアン法（線形和代入）を適用
row_ind, col_ind = linear_sum_assignment(cost_matrix)
# 枠順にソート
assignments = sorted(zip(col_ind, row_ind))  # 枠番号でソート

print("最適な割り当て:")
total = 0.0
for frame_index, item_index in assignments:
    value = weights[item_index][frame_index]
    item_name = item_names[item_index]
    print(f"枠 {frame_index + 1} → {item_name}（スコア {value}）")
    total += value

print(f"最大スコア合計: {total}")
