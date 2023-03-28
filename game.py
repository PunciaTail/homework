from sphinx import *
from create import *
from magician import *


def call_generic():
    input('전투를 시작합니다. 아무키나 누르세요.')

    while player.hp > 0 and monster.hp > 0:

        select = input("1마법 2공격")

        if select == '1':
            player.magic(monster)
            time.sleep(0.5)
            player.show_status()
            monster.show_status()
            time.sleep(1)
            if monster.hp == 0:
                print(f'{player.name}님 축하합니다. 승리하셨어요.')
                break
            monster.attack(player)
            time.sleep(0.5)
            player.show_status()
            monster.show_status()
            if player.hp == 0:
                print('You die')
                break

        elif select == '2':
            player.attack(monster)
            time.sleep(0.5)
            player.show_status()
            monster.show_status()
            time.sleep(1)
            if monster.hp == 0:
                print(f'{player.name}님 축하합니다. 승리하셨어요.')
                break
            monster.attack(player)
            time.sleep(0.5)
            player.show_status()
            monster.show_status()
            if player.hp == 0:
                print('You die')
                break

        else:
            print("알맞은 값을 입력하세요")

        if monster.hp == 0:
            print(f'{player.name}님 축하합니다. 승리하셨어요.')
            break

        elif player.hp == 0:
            print('You die')
            break

    return


if monster.name == 'sphinx':
    call_sphinx()
elif monster.name == 'magician':
    call_magician()
else:
    call_generic()
