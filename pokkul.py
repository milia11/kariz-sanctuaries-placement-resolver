from math import inf

import numpy as np
from scipy.optimize import linear_sum_assignment

class Pokkul:
    def __init__(self, name, hp=0, crit_dmg=0, atk=0, crit=0, defense=0, crit_resist=0, must_assign=False):
        self.name = name
        self.hp = hp
        self.crit_dmg = crit_dmg
        self.atk = atk
        self.crit = crit
        self.defense = defense
        self.crit_resist = crit_resist
        self.must_assign = must_assign

# 通常の枠15個 + 逃がし用の別枠2個（スコア無効）
NUM_MAIN_FRAMES = 15
NUM_ESCAPE_FRAMES = 2
# 15個の枠（各枠で重要視するステータスの重み）
frame_weights = [
    {"hp": 1.0, "crit_dmg": 1.0},
    {"atk": 1.0, "crit": 1.0},
    {"defense": 1.0, "crit_resist": 1.0},
    {"atk": 1.0, "crit_dmg": 1.0},

    {"hp": 1.0, "crit": 1.0},
    {"atk": 1.0, "defense": 1.0},
    {"defense": 1.0, "crit_resist": 1.0},
    {"atk": 1.0, "crit_dmg": 1.0},

    {"hp": 1.0, "crit": 1.0},
    {"atk": 1.0, "defense": 1.0},
    {"defense": 1.0, "crit_resist": 1.0},
    {"atk": 1.0, "defense": 1.0},

    {"hp": 1.0, "crit": 1.0},
    {"defense": 1.0, "crit_resist": 1.0},
    {"hp": 1.0, "crit_dmg": 1.0},
]
# escape用枠（何も重視しない、スコア常に0）
for _ in range(NUM_ESCAPE_FRAMES):
    frame_weights.append({})
# ポックルの一覧（例）
pokkuls = [
    Pokkul("ヒーラー", hp=386135, crit_dmg=33929, atk=118415, crit=42509, defense=99800, crit_resist=30036),
    Pokkul("タンク", hp=391179, crit_dmg=33929, atk=124000, crit=43893, defense=98210, crit_resist=30106),
    Pokkul("アシスト", hp=383848, crit_dmg=34268, atk=124000, crit=49651, defense=97620, crit_resist=29648),
    Pokkul("オリーサ", hp=401545, crit_dmg=36726, atk=123065, crit=51445, defense=99800, crit_resist=32624),
    Pokkul("ヴァルキリ", hp=472830, crit_dmg=35606, atk=124000, crit=55528, defense=99800, crit_resist=32844),
    Pokkul("ハナン", hp=389477, crit_dmg=36616, atk=124000, crit=64399, defense=99800, crit_resist=31470),
    Pokkul("メラー", hp=389477, crit_dmg=36616, atk=124000, crit=64399, defense=99800, crit_resist=31470),
    Pokkul("ネオ", hp=178010, crit_dmg=15124, atk=54836, crit=17224, defense=47417, crit_resist=13260),
    Pokkul("ぼたん", hp=222971, crit_dmg=15106, atk=59317, crit=17256, defense=43974, crit_resist=13241),
    Pokkul("リリス", hp=155691, crit_dmg=13151, atk=49934, crit=15127, defense=38423, crit_resist=11521),
    Pokkul("アカーシュ", hp=155691, crit_dmg=13151, atk=53978, crit=15127, defense=700, crit_resist=450),
    Pokkul("フィオナ", hp=410713, crit_dmg=30555, atk=115133, crit=41456, defense=90194, crit_resist=27449),
    Pokkul("テティス", hp=281723, crit_dmg=20364, atk=78621, crit=24111, defense=65920, crit_resist=17831),
    Pokkul("ハートネル", hp=274746, crit_dmg=18668, atk=77944, crit=21603, defense=54166, crit_resist=16421, must_assign=True),
    Pokkul("ニャロン", hp=389486, crit_dmg=36617, atk=124000, crit=64400, defense=99800, crit_resist=31470),
    Pokkul("スズネ", hp=237566, crit_dmg=20357, atk=82249, crit=25325, defense=59337, crit_resist=17748, must_assign=True),
    Pokkul("コルル", hp=255772, crit_dmg=22377, atk=91574, crit=27244, defense=63887, crit_resist=19416),
    Pokkul("アスリル", hp=285692, crit_dmg=20364, atk=85621, crit=24111, defense=62200, crit_resist=17830, must_assign=True),
    Pokkul("シラヌイ", hp=257485, crit_dmg=22171, atk=92377, crit=26352, defense=64070, crit_resist=19688),
    # Pokkul("カイドウ", hp=296440, crit_dmg=25790, atk=97288, crit=31381, defense=73654, crit_resist=23067, must_assign=True),
    Pokkul("ミア", hp=237569, crit_dmg=20357, atk=89910, crit=25326, defense=59337, crit_resist=17748, must_assign=True),
    Pokkul("ニャース", hp=238235, crit_dmg=20364, atk=85621, crit=24111, defense=62200, crit_resist=17830, must_assign=True),
    Pokkul("ベルベット", hp=257844, crit_dmg=22171, atk=92377, crit=26352, defense=64070, crit_resist=19688, must_assign=True),
    # Pokkul("ルリ", hp=3000, crit_dmg=1400, atk=1800, crit=200, defense=900, crit_resist=500),
    Pokkul("アイリス", hp=256612, crit_dmg=22551, atk=1800, crit=200, defense=63915, crit_resist=19437, must_assign=True),
    # （15以上必要）
]


def compute_score(pokkul, weight):
    return (
            pokkul.hp * weight.get("hp", 0) * 0.00001 +
            pokkul.crit_dmg * weight.get("crit_dmg", 0) * 0.0001 +
            pokkul.atk * weight.get("atk", 0)*100 +
            pokkul.crit * weight.get("crit", 0) * 0.0001 +
            pokkul.defense * weight.get("defense", 0)  +
            pokkul.crit_resist * weight.get("crit_resist", 0) * 0.001
    )


# スコア行列 (ポックル数 × 15)
num_pokkuls = len(pokkuls)
num_frames = len(frame_weights)

if sum(p.must_assign for p in pokkuls) > num_frames:
    raise ValueError("枠数より多くの must_assign=True ポックルがいます")

scores = np.zeros((num_pokkuls, num_frames))
for i, pokkul in enumerate(pokkuls):
    for j, weight in enumerate(frame_weights):
        scores[i, j] = compute_score(pokkul, weight)

# ハンガリアン法に向けてスコア最大化 → コスト最小化に変換
max_score = np.max(scores)
cost_matrix = max_score - scores

# ダミー列（割り当て回避）を追加する場合
if num_pokkuls > num_frames:
    extra = num_pokkuls - num_frames
    cost_matrix = np.pad(cost_matrix, ((0, 0), (0, extra)), constant_values=max_score)
    frame_weights += [{} for _ in range(extra)]  # ダミー枠のweight追加
    num_frames += extra

# must_assign の制約：通常はダミー枠禁止、ただし「逃がし枠」は許容
escape_frame_start = NUM_MAIN_FRAMES
escape_frame_end = NUM_MAIN_FRAMES + NUM_ESCAPE_FRAMES

for i, pokkul in enumerate(pokkuls):
    if pokkul.must_assign:
        # 全ダミー枠禁止
        for j in range(num_frames, cost_matrix.shape[1]):
            cost_matrix[i, j] = inf
        # 通常枠が全部埋まるとき、「逃がし枠」だけ許可
        for j in range(escape_frame_end, cost_matrix.shape[1]):
            cost_matrix[i, j] = inf

# 割り当て
row_ind, col_ind = linear_sum_assignment(cost_matrix)

# 結果出力
assignments = list(zip(row_ind, col_ind))
# 枠番号（f_idx）で昇順にソート
assignments.sort(key=lambda x: x[1])

print("最適な編成:")
total = 0.0
for p_idx, f_idx in assignments:
    pokkul = pokkuls[p_idx]
    if f_idx < NUM_MAIN_FRAMES:
        score = scores[p_idx][f_idx]
        print(f"枠 {f_idx + 1:2d} ← {pokkul.name}（スコア: {score:.1f}）")
        total += score
    elif f_idx < NUM_MAIN_FRAMES + NUM_ESCAPE_FRAMES:
        print(f"別枠        ← {pokkul.name}（※スコア無視）")
    # ダミー枠（使用しないポックル）は表示しない

print(f"最大スコア合計: {total:.1f}")
