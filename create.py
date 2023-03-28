import random
import time


class Character:
    def __init__(self, name, hp, power, mp):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.power = power

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def magic(self, other):
        if self.mp > 0:
            mg_damage = random.randint(self.mp - 4, self.mp + 7)
            other.hp = max(other.hp - mg_damage, 0)
            self.mp = max(self.mp - mg_damage, 0)
            print(f"{self.name}의 마법 공격! {other.name}에게 {mg_damage}의 데미지를 입혔습니다.")
            if self.mp < 0:
                self.mp == 0
        elif self.mp <= 0:
            self.mp == 0

        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")
        if self.mp >= 0:
            print(f"{self.name}의 상태: MP {self.mp}/{self.max_mp}")


class SubMonster:
    def __init__(self, name, list):
        self.name = name
        self.list = list


# 이름 설정
time.sleep(0.5)
print("이름을 입력하세요")
name = input()
time.sleep(0.5)
print(f'플레이어 생성: {name}')

monster = ['fairy', 'sphinx', 'magician']

# 몬스터 랜덤 생성
m_ran = random.choice(monster)
hp_ran = random.randrange(25, 40)
pw_ran = random.randrange(10, 35)

# 플레이어 생성
# 랜덤으로 몬스터 종류 변경
if name != '':
    player = Character(name, 30, 15, 20)
    monster = Character(m_ran, hp_ran, pw_ran, -1)
