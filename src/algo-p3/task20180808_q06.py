def print_hand(hand, name='ゲスト'):
    '''
    誰がじゃんけんで何を出したか
    Parameters
    ----------
    hand
        じゃんけんで出した手の形
    name='ゲスト'
        じゃんけんのプレイヤー(初期値は'ゲスト')
    Returns
    -------
    None
    '''

    hands = ['グー', 'チョキ', 'パー']


    print(name + 'は', hands[player_hand], 'を出した')


print('じゃんけんをはじめる')
player_name = input('名前を入力：')

print("何を出しますか？(0: グー 1: チョキ 2: パー)")


player_hand = int(input('数字で入力：'))

if player_name == '':

    print_hand(player_hand)
else:

    print_hand(player_hand, player_name)
