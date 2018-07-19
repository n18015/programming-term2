from tkinter import *
import math

# ウィンドウオブジェクト
w = None

# 現在位置
x = 200
y = 200

# 現在の向き(右向きを0度。分度器と同じ)
cur_deg = 0

# 曲がる方向
left = 1
right = -1

# 画面の初期化
def init_screen():
    global w
    w = Canvas(Tk(), width=400, height=400)
    w.pack()

# 線を引く
def draw_line(pixels):
    global w, x, y, cur_deg
    start_x = x
    start_y = y
    end_x = start_x + round(round(math.cos(math.radians(cur_deg)), 2) * pixels, 0)
    end_y = start_y + (round(round(math.sin(math.radians(cur_deg)), 2) * pixels, 0)) * -1
    # 直線を描画
    w.create_line(start_x, start_y, end_x, end_y)
    x = end_x
    y = end_y

# 回転する
def turn(direction, degree):
    global cur_deg
    cur_deg += degree * direction

# 画面を起動(変更しないこと)
init_screen()

# メイン処理(ここを埋める)
draw_line(100)
turn(right, 90)
draw_line(100)
turn(right, 90)
draw_line(100)
turn(right, 90)
draw_line(100)

# closeされるまで待機(変更しないこと)
mainloop()
