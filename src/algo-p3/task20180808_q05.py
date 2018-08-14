def print_hand(hand, name='ゲスト'):
    '''
    誰がじゃんけんで何を出したかを取得
    Parameters
    ----------
    hand
        じゃんけんで出した手
    name='ゲスト'
        じゃんけんのプレイヤー(初期値は'ゲスト')
    Returns
    -------
    None
    '''
    print(name + 'は' + hand + 'を出しました')


print('じゃんけんをはじめる')


player_name = input('名前を入力：')


if player_name == '':
    print_hand('グー')

else:
    print_hand('グー', player_name)
