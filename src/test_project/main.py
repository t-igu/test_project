import pandas as pd

# 辞書を作成
data = {
    '名前': ['田中', '渡辺', '具志堅'],
    '年齢': [34, 23, 68],
    '出身地': ['大阪', '名古屋', '沖縄']
}

# 辞書を DataFrame 型へ変換
df = pd.DataFrame(data)
print(df)