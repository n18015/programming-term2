cur_pos = [0, 0] # 現在位置
direction = [1, 0] # いま右に向いてるから[1, 0]

def go_forward():
    global cur_pos, direction
    cur_pos[0] += direction[0]
    cur_pos[1] += direction[1]
    print("現在位置はx={0},y={1}です。".format(cur_pos[0], cur_pos[1]))

def turn_right():
    global direction
    if direction == [0, 1]:
        # いま上に向いていたら右に向きを変える
        direction = [1, 0]
    elif direction == [1, 0]:
        # いま右に向いていたら下に向きを変える
        direction = [0, -1]
    elif direction == [0, -1]:
        # いま下に向いていたら左に向きを変える
        direction = [-1, 0]
    else:
        # いま左に向いていたら上に向きを変える
        direction = [0, 1]

def turn_left():
    global direction
    if direction == [0, 1]:
        # いま上に向いていたら左に向きを変える
        direction = [-1, 0]
    elif direction == [-1, 0]:
        # いま左に向いていたら下に向きを変える
        direction = [0, -1]
    elif direction == [0, -1]:
        # いま下に向いていたら右に向きを変える
        direction = [1, 0]
    else:
        # いま左に向いていたら上に向きを変える
        direction = [0, 1]

# メイン処理
while cur_pos != [5, -5]:
    turn_right()
    go_forward()
    turn_left()
    go_forward()
