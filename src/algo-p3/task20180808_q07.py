def validate(hand):
    '''
    じゃんけんで出した手の形を正しく出力させる関数(0,1,2以外で構文エラーが出ないよう)

    Parameters
    ----------
    hand
        じゃんけんで出した手

    Returns
    -------
    False
        不正入力
    True
        正しい入力
    '''
    if hand < 0:
        return False
    elif hand > 2:
        return False
    else:
        return True


def print_hand(hand, name='ゲスト'):
    '''
    誰がじゃんけんで何を出したかを取得

    Parameters
    ----------
    hand
        じゃんけんで出した手の形
    name='ゲスト'
        プレイヤーの名前(ゲスト)

    Returns
    -------
    None
    '''
    hands = ['グー', 'チョキ', 'パー']
    print(name + 'は' + hands[hand] + 'を出しました')


print('じゃんけんをはじめます')
player_name = input('名前を入力：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力：'))

if validate(player_hand):
    if player_name == '':
        print_hand(player_hand)
    else:
        print_hand(player_hand, player_name)

else:
    print("正しい数値を入力")
