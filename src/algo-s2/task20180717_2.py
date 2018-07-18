x = 0 # 現在の横位置
y = 0 # 現在の縦位置

dir_x = 1 # いま右に向いてるから+1
dir_y = 0 # いま上にも下にも向いてないから0

def go_forward():
    global x, y, dir_x, dir_y
    x += dir_x
    y += dir_y
    print("現在位置はx={0},y={1}です。".format(x, y))

def turn_left():
    global x, y, dir_x, dir_y
    if dir_y == 1:
        # いま上に向いていたら左に向きを変える
        dir_x = -1
        dir_y = 0
    elif dir_y == -1:
        # いま下に向いていたら右に向きを変える
        dir_x = 1
        dir_y = 0
    else:
        if dir_x == 1:
            # いま右を向いていたら上に向きを変える
            dir_x = 0
            dir_y = 1
        elif dir_x == -1:
            # いま左を向いていたら下に向きを変える
            dir_x = 0
            dir_y = -1
            
def turn_right():
    global x, y, dir_x, dir_y
    if dir_y == 1:
        # いま上に向いていたら右に向きを変える
        dir_x = 1
        dir_y = 0
    elif dir_y == -1:
        # いま下に向いていたら左に向きを変える
        dir_x = -1
        dir_y = 0
    else:
        if dir_x == 1:
            # いま右を向いていたら下に向きを変える
            dir_x = 0
            dir_y = -1
        elif dir_x == -1:
            # いま左を向いていたら上に向きを変える
            dir_x = 0
            dir_y = 1

#メイン処理
go_forward()
turn_left()
go_forward()
turn_right()
go_forward()
