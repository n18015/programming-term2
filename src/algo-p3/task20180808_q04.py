def print_hand(hand, name='ゲスト'):
    '''
    誰がじゃんけんで何を出した
    Parameters
    ----------
    hand
        じゃんけんで出した手の形
    name='ゲスト'
        じゃんけんのプレイヤー(初期値は'ゲスト')
    '''
    print(name + 'は' + hand + 'を出しました')


print_hand('グー')
