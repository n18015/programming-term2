from enemy import Enemy


# Enemyクラスを継承し、ZakoCharaクラスを作成します。
class ZakoChara(Enemy):
    # コンストラクタ(__init__())のみを、Enemyクラスのものをそのままコピーして貼り付けてください。attack()メソッドは不要です。
    def __init__(self, name):
        """
        コンストラクタ
        Parameters
        ----------
        name : str
            敵の名前
        Returns
        -------
        自分自身のインスタンス
        """

    class Enemy:
        def __init__(self, name):
            """
            コンストラクタ
            Parameters
            ----------
            name : str
            敵の名前
            Returns
            -------
            自分自身のインスタンス
            """
            self.name = name
        # 元々のコンストラクタをZakoCharaクラスにそのままコピーした後で、以下の値全てに1を代入するよう変更してください。
            self.hp = 1
            self.min_damage = 1
            self.max_damage = 1
            self.freq = 1
