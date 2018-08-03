# 成績データを辞書型で定義
records = {
    'Tanaka':72, 'Ymada':65, 'Hirata':100,
    'Akai':56, 'Fukuda':66, 'Sakai':80 }
# 合計を求める ---(1)
sum_v = 0
for v in records.values():  #recordsの値だけを順に取得
    sum_v += v
# 平均点を計算して結果を表示
ave_v = sum_v / len(records)
print("合計点:", sum_v)
print("平均点:", ave_v)

# 成績データの一覧と平均点との差を表示 ---(2)
fmt = "| {0:<7} | {1:>4} | {2:>5}"  # 7文字左寄せ、4文字右寄せ、5文字右寄せと指定
print("|名前    |点数|差")
for name, v in sorted(records.items()):
    # 平均点との差を求める
    diff_v = v - ave_v
    # 小数点以下を丸める --- (3)
    diff_v = round(diff_v, 1) # diff_vの値を小数点以下1位になるように四捨五入
    # 書式にそって出力 ---(4)
    print(fmt.format(name, v, diff_v))
