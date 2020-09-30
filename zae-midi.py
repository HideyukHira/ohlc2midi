import pandas as pd
import pretty_midi

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
print(df['終値'].max())
print(df['終値'].min())
#最大値から最小値を引いて 36音階分で割る ＝ １ノート増分のUSD価格算出
step = (df['終値'].max() - df['終値'].min()) / 48
print( step )
#USD価格から最小値を引いて、STEP値で割ることで、ノートナンバーを取得
dfmin = df['終値'].min()
#NOTENUM列に代入
df["NOTENUM"] = ( (df['終値'] - dfmin) / step ).round().astype(int)
print(df[['終値','NOTENUM']].describe() )
print(df[['終値','NOTENUM']] )



# pretty_midiオブジェクトを作ります
pm = pretty_midi.PrettyMIDI(resolution=960, initial_tempo=120)
#instrumentはトラックみたいなものです。
instrument = pretty_midi.Instrument(0)

midi_start = 0
midi_end = 1
#LOOPでノートナム
for item in df['NOTENUM'].iloc[::-1]:
  #print("item :", item,"\n")
  # TODO CHECK can nodenumber
  #pretty_midi.Note(velocity, pitch, start, end)
  print(item)
  note = pretty_midi.Note(velocity=100, pitch=item+24, start=midi_start, end=midi_end)
  instrument.notes.append(note)
  midi_start +=1
  midi_end +=1


pm.instruments.append(instrument)
pm.write('test.mid') #midiファイルを書き込みます。





