from day15.model.character_abc import

class Warrior(Character):
    def __init__(self, name, health):
        super().__init__(name, health)

#super().는 상속의 의미라서     self.name = name , self.health = health를 줄여 쓰는 셈

        self.rage = 0

    def attack(self):
        print('검 휘두르기')
        self.rage += 10

    def defend(self):
        print('방패로 막기')

    def special(self):
        if self.rage == 100:
            print('분노 모드')
            self.rage = 0
        else:
            print(f"분노 게이지가 {100-self.rage} 모자릅니다.")
