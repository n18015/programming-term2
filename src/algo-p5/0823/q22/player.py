import field_map
import sys
import random
from enemy import Enemy


class Player:
    def __init__(self, name):
        """
        コンストラクタ
        Parameters
        ----------
        name : str
            プレイヤーの名前
        Returns
        -------
        自分自身のインスタンス
        """
        self.name = name
        self.cur_pos = 0
        self.hp = 100
        self.max_hp = 100
        self.min_damage = 4
        self.max_damage = 7
        self.freq = 10
        self.plant_nums = 10
        self.exp = 0
        self.level = 1

    def choose_action_in_field(self):
        """
        フィールド中での操作を選択する
        Parameters
        ----------
        なし
        Returns
        -------
        なし
        """
        print()

        print("何をしますか?")

        cmd_num = input("1:サイコロを振る、2:現在の状態を確認する、9:ゲームを終了する>> ")

        if cmd_num == "1":

            self.move()
        elif cmd_num == "2":

            self.show_status()
        elif cmd_num == "9":

            self.quit_game()

    def move(self):
        """
        動く(サイコロを振る行為を含む)
        Parameters
        ----------
        なし
        Returns
        -------
        なし
        """
        dice_num = field_map.shake_dice()

        self.go_forward(dice_num)

    def go_forward(self, cells):
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
        self.cur_pos += cells

        print("現在位置は" + str(self.cur_pos) + "です。")

        event_nm = field_map.get_event(self.cur_pos)

        if event_nm == "GoMoreForward":

            self.go_more_forward(2)
        elif event_nm == "GoBack":

            self.go_back(3)
        elif event_nm == "GoBackToStart":

            self.go_back_to_start()

    def go_more_forward(self, cells):
        """
        出た目の分さらに前に進む
        Parameters
        ----------
        cells : int
            進むマス目の数
        Returns
        -------
        なし
        """
        print("イベント発生！" + str(cells) + "マスさらに進みます。")

        self.go_forward(cells)

    def go_back(self, cells):
        """
        出た目の分後ろに戻る
        Parameters
        ----------
        cells : int
            戻るマス目の数
        Returns
        -------
        なし
        """
        print("イベント発生！" + str(cells) + "マス後ろに戻ります。")

        self.go_forward((cells * -1))

    def go_back_to_start(self):
        """
        出た目の分後ろに戻る
        Parameters
        ----------
        なし
        Returns
        -------
        なし
        """
        print("イベント発生！振り出しに戻ってしまいます！")

        self.go_forward((self.cur_pos * -1))

    def show_status(self):
        """
        現在の状態を表示する
        Parameters
        ----------
        なし
        Returns
        -------
        なし
        """
        print(self.name + "の現在位置は" + str(self.cur_pos) + "、HPは"
              + str(self.hp) + "です。")

    def battle(self, enemy):
        """
        敵とたたかう
        Parameters
        ----------
        enemy : Enemy
            敵のオブジェクト
        Returns
        -------
        なし
        """
        print("イベント発生！" + enemy.name + "があらわれた！")

        while enemy.hp > 0:

            if self.attack(enemy):
                break

            if not enemy.attack(self):
                print(self.name + "はしんでしまった!世界は闇に包まれてしまった...")
                sys.exit()

        print(self.name + "は" + enemy.name + "を倒した!")

    def attack(self, enemy):
        """
        敵を攻撃する
        Parameters
        ----------
        enemy : Enemy
            敵のオブジェクト
        Returns
        -------
        bool
            True:敵を倒した、False:敵がまだ生きている
        """
        damage = random.randint(self.min_damage, self.max_damage)

        is_critical = False

        rand_num = random.randint(1, self.freq)
        if rand_num % self.freq == 0:
            is_critical = True

        print(self.name + "のこうげき!")

        if is_critical:
            print("かいしんのいちげき!!")
            damage *= 2

        enemy.hp -= damage

        if enemy.hp > 0:
            print(enemy.name + "に" + str(damage) + "のダメージを与えた!"
                  + enemy.name + "のHPは" + str(enemy.hp) + "です。")
            return False
        else:
            print(enemy.name + "に" + str(damage) + "のダメージを与えた!"
                  + enemy.name + "のHPは0です。")
            return True

    def quit_game(self):
        """
        ゲームを終了する
        Parameters
        ----------
        なし
        Returns
        -------
        なし
        """
        cmd_str = input("ゲームの状態はセーブされません。終了しますか?(y/n) ")

        if cmd_str.upper() == "Y":
            sys.exit()


if __name__ == '__main__':

    kevin = Player("ケビン")

    enemy = Enemy("スラスラ")

    kevin.battle(enemy)

    kevin.show_status()
