import random

def validate(hand):
    '''
    じゃんけんで出した手の形を正しく出力させる関数(0,1,2以外で構文エラーが出ないよう)

    Parameters
    ----------
    hand
        じゃんけんで出した手の形

    Returns
    -------
    False
        不正入力
    True
        正しい入力
    '''
    if hand < 0 or hand > 2:
        return False
    return True


def print_hand(hand, name='ゲスト'):
    '''
    誰がじゃんけんで何を出したかを取得

    Parameters
    ----------
    hand
        じゃんけんで出した手の形
    name-'ゲスト'
        プレイヤーの名前(ゲスト)

    Returns
    -------
    None
    '''
    hands = ['グー', 'チョキ', 'パー']
    print(name + 'は' + hands[hand] + 'を出しました')


def judge(player, computer):
    '''
    playerとcomputerの対戦結果を出力するための関数

    Parameters
    ----------
    player
        ユーザーが入力したじゃんけん
    computer
        プリセットされたじゃんけんを出力(random関数によりランダムに出力される)

    Returns
    -------
    "引き分け"
        playerとcomputerが出力したものが同じである引き分け
    "勝ち"
        playerが入力した数値がcomputerに勝っていたplayerの勝ち
    "負け"
        playerが入力した数値がcomputerに負けていたplayerの負け
    '''
    if player == computer:
        return '引き分け'
    elif player == 0 and computer == 1:
        return '勝ち'
    elif player == 1 and computer == 2:
        return '勝ち'
    elif player == 2 and computer == 0:
        return '勝ち'
    else:
        return '負け'


print('じゃんけんをはじめます')
player_name = input('名前を入力：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力：'))

if validate(player_hand):
    computer_hand = random.randint(0, 2)
    if player_name == '':
        print_hand(player_hand)
    else:
        print_hand(player_hand, player_name)

    print_hand(computer_hand, 'コンピューター')

    result = judge(player_hand, computer_hand)
    print('結果は' + result + 'でした')
else:
    print('正しい数値を入力')
