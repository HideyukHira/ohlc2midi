import pandas as pd


# read csv assgin to df
df = pd.read_csv('usdzar.csv')

#reverse sort
# print(  (df['終値']).iloc[::-1]   )




# 表示名	説明	Pandasで相当する関数
# count	データの個数を表します。	DataFrame.count,Series.count
# mean	数値データの平均を表します。	DataFrame.mean,Series.mean
# std	数値データの標準偏差を表します。	DataFrame.std, Series.std
# min	最小値を表します。	DataFrame.min,Series.min
# max	最大値を表します。	DataFrame.max,Series.max
# 25%,50%,75%	四分位数を表します。(区切る部分はpercentiles引数で変更可能)	DataFrame.quantile,Series.quantile
print(df['終値'].describe())