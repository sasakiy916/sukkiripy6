class Hero:
    def __init__(self,name="松田",hp=32):
        self.name = name
        self.hp = hp

    def sleep(self,hours):
        print(f"{self.name}は{hours}時間ネタ")
        self.hp += hours

# ゲーム開始
print("スッキリファンタジーⅫ ～金色の理想郷～")
h = Hero()
h.sleep(3)
print(f"{h.name}のHPは現在{h.hp}です")