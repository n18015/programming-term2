from enemy import Enemy


# Enemyクラスを継承し、BossCharaクラスを作成します。
class BossChara(Enemy):
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
        super().__init__(name)
        # self.hpに200を、self.min_damageに8を、self.max_damageに13を、self.freqに10を代入してください。
        self.hp = 200
        self.min_damage = 8
        self.max_damage = 13
        self.freq = 10

