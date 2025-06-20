## カリツの伝説の紀元聖物の最適配置問題を解きます。
### 注意
- 使用中の聖物はコメントアウトしてください
- `weights`の行列は正方行列である必要があります。

### 実行
```shell
python calculate.py
```

### 実行に必要な依存ライブラリ
pythonを使用しています。  `scipy` が必要です。インストールされていない場合は以下でインストールできます：

```bash
pip install scipy
```

### 備考
- Hungarian法の処理は、`scipy.optimize.linear_sum_assignment()` で行っています。
- スコア部分の重み付けを変更することで最適配置は変わります。 (コードはM攻撃とM防御無視を優先した構成)
- 紀元聖物の6個配置枠がある状態でのコードです。
- 新しい聖物が実装された場合は枠を含めて追加修正する必要があります。
```
 1 2
3 4 5
6
```

### 実行結果メモ
- 6個枠がある場合でエーギル王の明灯を使用中
```
最適な割り当て:
枠 1 → ユピテル王の法環（スコア 18150.0）
枠 2 → アストラ王の鎧（スコア 11205.0）
枠 3 → 至上マッシュの扇（スコア 6778.0）
枠 4 → 極盛マッシュの杖（スコア 0.0）
枠 5 → エーギル王の戦矛（スコア 9502.0）
枠 6 → エーギル王の戦鎧（スコア 19560.0）
最大スコア合計: 65195.0

```

- 6個枠がある状態で極上マッシュの扇を使用中
```
最適な割り当て:
枠 1 → エーギル王の明灯（スコア 22020.0）
枠 2 → アストラ王の鎧（スコア 11205.0）
枠 3 → エーギル王の戦矛（スコア 7450.0）
枠 4 → ユピテル王の法環（スコア 0.0）
枠 5 → 極盛マッシュの杖（スコア 7275.0）
枠 6 → エーギル王の戦鎧（スコア 19560.0）
最大スコア合計: 67510.0

```