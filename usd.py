import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# read csv assgin to df
df = pd.read_csv('usdzar.csv')
df.plot()
plt.show()
# pandas to_datetime(df['日付']) ,string to timestayke
df["time"] = pd.to_datetime(df['日付'])
# print(df["time"])

# 移動平均線の計算
ma_25d = df['終値'].rolling(window=25).mean()
ma_75d = df['終値'].rolling(window=75).mean()

# データフレームの列に移動平均線を追加
df['移動平均線(25日)'] = ma_25d
df['移動平均線(75日)'] = ma_75d

# 移動平均のクロス確認
cross = ma_25d > ma_75d
golden = (cross != cross.shift(1)) & (cross == True)
dead = (cross != cross.shift(1)) & (cross == False)

# ゴールデンクロス・デッドクロスの発生位置（要素番号）をリストに格納
index_g = [i for i, x in enumerate(golden) if x == True]
index_d = [i for i, x in enumerate(dead) if x == True]

# グラフにプロット
ax = df['終値'].plot(color="blue", label="Close")
ma_25d.plot(ax=ax, ls="--", color="red", label="MA 25d")
ma_75d.plot(ax=ax, ls="--", color="green", label="MA 75d")
# df.iloc[index_g, 5].plot(ax=ax, ls='', marker='^', ms='10', color="green", label="Golden cross")
# df.iloc[index_d, 5].plot(ax=ax, ls='', marker='v', ms='10', color="red", label="Dead cross")
ax.grid()
ax.legend()

# print dataframe
print(golden)
