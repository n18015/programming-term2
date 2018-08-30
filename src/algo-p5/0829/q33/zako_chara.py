from enemy import Enemy


class ZakoChara(Enemy):
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
        # 名前の設定部分は継承元のenemyクラスのコンストラクタと全く同じことをしています。下記self.nameに代入する行を削除しましょう。
        # 親クラスのコンストラクタを呼び出します。super().__init__(name)を呼び出します。
        super().__init__(name)
        self.hp = 10
        self.min_damage = 2
        self.max_damage = 4
        self.freq = 30

