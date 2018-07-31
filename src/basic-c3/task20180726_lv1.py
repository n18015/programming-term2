# 定義達
import random
saikoro = 0
susumu = 0
# 関数達
def shake_dice():
    """
    サイコロの目の数
    Parameters
    ----------
    shake_dice : int
        サイコロの値
    Returns
    -------
    saikoro : int
        サイコロの目
    """
    saikoro = random.randint(1, 6)
    return saikoro
def go_forword(susumu):
    """
    今までのサイコロの目の合計数
    Parameters
    ----------
    go_forword : int
    サイコロの目の合計
    Returns
    -------
    susumu : int
        サイコロの合計値
    """
    susumu += saikoro
    return susumu

while susumu < 10:
    enter = input("サイコロを振って\n(※ enterkey押すだけ)")
    if enter != "":
        continue
    saikoro = shake_dice()
    susumu = go_forword(susumu)
    if susumu < 10:
        print("{}が出ました。現在位置{}はです".format(saikoro, susumu))
        continue
    break
print("{}が出た。おめでとう、ゴール!".format(saikoro))
help(shake_dice)
help(go_forword)
