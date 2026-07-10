class Creature:
    def __init__(self, name, init, ac, hp):
        self.name = name
        self.init = init
        self.ac = ac
        self.hp = hp
    def modifyHp(self, amount):
        self.hp += amount
        if self.hp <= 0:
            print(f"💀  {self.name} испустил дух.")
            return False
        return True
    