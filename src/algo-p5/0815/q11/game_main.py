
import field_map

# 変数定義部
cur_pos = 0 # 現在の位置

# 関数定義部
def go_forward(cells):
    """
    前に進む
    Parameters
    ----------
    cells : int
        進むマス目の数
    Returns
    -------
    なし
    """
    # 現在位置をグローバル参照する
    global cur_pos

    # 引数のマス目だけ進む
    cur_pos += cells

    # 現在位置を表示
    print("現在位置は" + str(cur_pos) + "です。")

# 以下メイン処理
if __name__ == '__main__':
    # 開始メッセージを表示
    print("すごろくゲーム、Start!!")

    # ゴールに到達するまでサイコロを投げて進む行為を繰り返す
    while cur_pos < field_map.goal_pos:
        # サイコロを振る
        dice_num = field_map.shake_dice()

        # 出た目の分だけ進む
        go_forward(dice_num)

    # ゴール到達のメッセージを表示
    print("ゴールしました。おめでとうございます!")
