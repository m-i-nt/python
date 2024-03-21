from day15.model.warrior import Warrior
from day15.model.mage import Mage

print('메가 게임')

character_number = input('캐릭터를 선택하세요(1번 전사, 2번 마법사, 3번 궁수)')
name = input('이름을 넣어주세요:')
choice = {
    "1": Warrior(name, 200),
    '2': Mage(name, )
}

while True:
    selected = input('1.공격 2.방어 3.특수능력')
    if selected == '1':
        character.attack()
    elif selected == '2':
        character.defend()
    elif selected == '3':
        character.special()

#class 와 oop 프로그래밍은 c언어를 제외한 대부분의 언어의 공통점

#class 설계가 어려워서 나온 SOLID 원칙