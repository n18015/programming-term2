def print_hand(hand, name):
    '''
    誰がじゃんけんで何を出したか
    Parameters
    ----------
    hand
        じゃんけんで出した手
    name
        じゃんけんプレイヤー
    '''

    print(name, "は", hand, "を出しました")

print_hand('グー', 'ななしのたろう')

print_hand('パー', 'コンピューター')
