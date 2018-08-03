# 辞書型のテータ（果物名と値段）に変数に代入
fruits = {
    "バナナ": 300, "オレンジ": 240,
    "イチゴ": 350, "マンゴー": 400 }

# 辞書型のデータ一覧を表示
for name, price in fruits.items(): # ---(1)
    # 画面に出力
    s = "{0}は、{1}です。".format(name, price)
    print(s)
