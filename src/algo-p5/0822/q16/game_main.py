import field_map
from player import Player

cur_pos = 0  # 現在の位置

if __name__ == '__main__':

    print("すごろくゲーム、Start!!")

    p_name = input("プレイヤーの名前を教えてください>> ")

    hero = Player(p_name)

    print("やあ、" + hero.name + "!旅をはじめよう!")

    while hero.cur_pos < field_map.goal_pos:

        dice_num = field_map.shake_dice()

        hero.go_forward(dice_num)

    print("ゴールしました。おめでとうございます!")
