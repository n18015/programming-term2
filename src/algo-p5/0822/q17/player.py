import field_map
# sysパッケージをimportしてください。
import sys


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

    # choose_action_in_field()メソッドを定義します。引数はselfのみです。
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
        # 見やすさのために、空白行を表示してください。引数なしのprintで構いません。
        print(" ")

        # 「何をしますか?」を表示してください。
        print("何をしますか?")

        # input()関数を用いて、「1:サイコロを振る、2:現在の状態を確認する、9:ゲームを終了する>> 」
        # を表示し、入力された値をcmd_num変数に代入してください。
        cmd_num = input("1:サイコロを振る、2:現在の状態を確認する、9:ゲームを終了する>> ")
        cmd_num = int(cmd_num)
        # cmd_numの値によって条件分岐します。(cmd_numはintに変換しても良いですが、文字列のままでも構いません。)
        if cmd_num == 1:
            # cmd_numが1のとき、下記で追加したmove()メソッドを呼び出します。
            self.move()
        if cmd_num == 2:
            # cmd_numが2のとき、下記で追加したshow_status()メソッドを呼び出します。
            self.show_status()
        if cmd_num == 9:
            # cmd_numが9のとき、下記で追加したquit_game()メソッドを呼び出します。
            self.quit_game()

    # moveメソッドを定義します。引数はselfのみです。
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
        # サイコロを振ります。元のコード dice_num = field_map.shake_dice()をそのままここに移動します。
        dice_num = field_map.shake_dice()

        # go_forwardを引数にdice_numを与えて呼び出します。同じクラスのメソッドを呼び出すため、self.を付けて呼び出します。
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
        # 引数のマス目だけ進む
        self.cur_pos += cells

        # 現在位置を表示
        print("現在位置は" + str(self.cur_pos) + "です。")

        # 止まったマス目のイベントを取得する
        event_nm = field_map.get_event(self.cur_pos)

        if event_nm == "GoMoreForward":
            # 2マスさらに前に進む
            self.go_more_forward(2)
        elif event_nm == "GoBack":
            # 3マス戻る
            self.go_back(3)
        elif event_nm == "GoBackToStart":
            # 振り出しに戻る
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

        # 引数で渡された目の分だけ前に進む
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

        # 引数で出た目の分だけ前に戻る(引数に-1を掛けることで戻る動作をしている)
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

        # 現在位置の分だけ前に戻ることで振り出しに戻る動作をする(引数に-1を掛けることで戻る動作をしている)
        self.go_forward((self.cur_pos * -1))

    # show_statusメソッドを定義します。引数はselfのみです。
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
        # 「(self.name)の現在位置は(self.cur_pos)です。」の形式でプレイヤーの状態を表示する。
        print(self.name, "の現在位置は", self.cur_pos, "です。")

    # quit_gameメソッドを定義します。引数はselfのみです。
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
        cmd_str = input("ゲームの状態はセーブされません。終了しますか?(y/n)")

        if cmd_str == "y" or "Y":
            sys.exit(0)
