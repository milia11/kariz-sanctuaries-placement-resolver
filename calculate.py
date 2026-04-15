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
                self.bin_sho * (1 + 1) +
                self.sho_geki +
                self.bou_gyo_mu_shi * 1 +
                self.kou_geki
                +
                self.tai_ryoku * 0.0000001 +
                self.katsu_ryoku * 0.0000001 +
                self.sei_ki * 2 * 0.0000001

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
        Sanctuaries(sho_geki=7725, bou_gyo=12900),
        Sanctuaries(kou_geki=2550, bou_gyo=12450),
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
        Sanctuaries(sho_geki=8805, bou_gyo=23592),
        Sanctuaries(kou_geki=2550, bou_gyo=23142),
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
        Sanctuaries(sho_geki=5250, bou_gyo=12900),
        Sanctuaries(kou_geki=15379, bou_gyo=12450),
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
        Sanctuaries(sho_geki=9952, bou_gyo=27012),
        Sanctuaries(kou_geki=2550, bou_gyo=26562),
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
        Sanctuaries(sho_geki=5250, bou_gyo=12900),
        Sanctuaries(kou_geki=19560, bou_gyo=12450),
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
        Sanctuaries(sho_geki=11460, bou_gyo=31620),
        Sanctuaries(kou_geki=2550, bou_gyo=31170),
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
        Sanctuaries(sho_geki=5250, bou_gyo=12900),
        Sanctuaries(kou_geki=2550, bou_gyo=12450),
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
        Sanctuaries(sho_geki=5250, bou_gyo=33487),
        Sanctuaries(kou_geki=21225, bou_gyo=33037),
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
        Sanctuaries(sho_geki=11460, bou_gyo=31620),
        Sanctuaries(kou_geki=2550, bou_gyo=31620),
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
        Sanctuaries(sho_geki=5250, bou_gyo=12900),
        Sanctuaries(kou_geki=2550, bou_gyo=12900),
        Sanctuaries(kyo_ko=2550, kyo_ko_tei_ko=18270),
    ],
    "ラケシス王の大剣": [
        Sanctuaries(bin_sho=4800, sei_ki=5850),
        Sanctuaries(kou_bou=7650, kyo_ko_tei_ko=19507),
        Sanctuaries(tai_ryoku=5850, bou_gyo_mu_shi=12990),
        Sanctuaries(katsu_ryoku=15907, kyo_ko=12045),
        Sanctuaries(sho_geki=4800, bou_gyo=39832),
        Sanctuaries(kou_geki=23070, bou_gyo=39832),
        Sanctuaries(kou_bou=7650, sei_ki=5850),
        Sanctuaries(tai_ryoku=5850, bin_sho=4800),
        Sanctuaries(katsu_ryoku=15907, bou_gyo_mu_shi=12990),
        Sanctuaries(kyo_ko=12045, kyo_ko_tei_ko=19507),
        Sanctuaries(sho_geki=5250, bou_gyo=40282),
        Sanctuaries(kou_geki=23070, bou_gyo=40282),
        Sanctuaries(kyo_ko=12045, kyo_ko_tei_ko=19507),
    ],
    "エーギル王の幻鏡": [
        Sanctuaries(bin_sho=14745, sei_ki=13905),
        Sanctuaries(kou_bou=7650, kyo_ko_tei_ko=5850),
        Sanctuaries(tai_ryoku=5850, bou_gyo_mu_shi=2550),
        Sanctuaries(katsu_ryoku=16605, kyo_ko=12985),
        Sanctuaries(sho_geki=14745, bou_gyo=42555),
        Sanctuaries(kou_geki=2550, bou_gyo=42555),
        Sanctuaries(kou_bou=7650, sei_ki=13905),
        Sanctuaries(tai_ryoku=5850, bin_sho=14745),
        Sanctuaries(katsu_ryoku=16605, bou_gyo_mu_shi=2550),
        Sanctuaries(kyo_ko=12985, kyo_ko_tei_ko=5850),
        Sanctuaries(sho_geki=15195, bou_gyo=43005),
        Sanctuaries(kou_geki=2550, bou_gyo=43005),
        Sanctuaries(kyo_ko=12985, kyo_ko_tei_ko=5850),
    ],
    "豊穣マッシュの技": [
        Sanctuaries(bin_sho=15735, sei_ki=14692),
        Sanctuaries(kou_bou=18585, kyo_ko_tei_ko=22365),
        Sanctuaries(tai_ryoku=14692, bou_gyo_mu_shi=15150),
        Sanctuaries(katsu_ryoku=8550, kyo_ko=2550),
        Sanctuaries(sho_geki=4800, bou_gyo=12450),
        Sanctuaries(kou_geki=2550, bou_gyo=12450),
        Sanctuaries(kou_bou=18585, sei_ki=14692),
        Sanctuaries(tai_ryoku=14692, bin_sho=15735),
        Sanctuaries(katsu_ryoku=8550, bou_gyo_mu_shi=15150),
        Sanctuaries(kyo_ko=2550, kyo_ko_tei_ko=22365),
        Sanctuaries(sho_geki=4800, bou_gyo=12900),
        Sanctuaries(kou_geki=2550, bou_gyo=12900),
        Sanctuaries(kyo_ko=2550, kyo_ko_tei_ko=22365),
    ],
    # "ラケシス王の飛靴": [#Lv25
    #     Sanctuaries(bin_sho=3970, sei_ki=4770),
    #     Sanctuaries(kou_bou=6330, kyo_ko_tei_ko=19296),
    #     Sanctuaries(tai_ryoku=4770, bou_gyo_mu_shi=13660),
    #     Sanctuaries(katsu_ryoku=14800, kyo_ko=12628),
    #     Sanctuaries(sho_geki=3970, bou_gyo=39274),
    #     Sanctuaries(kou_geki=24835, bou_gyo=39274),
    #     Sanctuaries(kou_bou=6330, sei_ki=4770),
    #     Sanctuaries(tai_ryoku=14692, bin_sho=3970),
    #     Sanctuaries(katsu_ryoku=14800, bou_gyo_mu_shi=13660),
    #     Sanctuaries(kyo_ko=12628, kyo_ko_tei_ko=19296),
    #     Sanctuaries(sho_geki=4340, bou_gyo=39644),#sho_geki:upper, bou_gyo:upper
    #     Sanctuaries(kou_geki=24835, bou_gyo=39644),
    #     Sanctuaries(kyo_ko=12628, kyo_ko_tei_ko=19296),
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
