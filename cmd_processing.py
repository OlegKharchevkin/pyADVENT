from Player import Player
from random import randint


def cnd_processing(obj: str, conditions: list, messages: dict, objects: dict, player: Player, _print, _input):
    for index, i in enumerate(conditions):
        buf = True
        if i[0] == 'o':
            if i[2] == '****':
                buf = obj == ''
            else:
                buf = obj == i[2]
        elif i[0] == 'a' or i[0] == 'h':
            if i[2] != '':
                buf = i[2] in player.objects_db[player.location]
            else:
                buf = obj in player.objects_db[player.location]
        elif i[0] == 't':
            if i[2] != '':
                buf = i[2] in player.inventory
            else:
                buf = obj in player.inventory
        elif i[0] == '%':
            buf = randint(0, 99) < i[2]
        elif i[0] == 'p':
            if i[2] != '':
                buf = player.objects_states[obj] == i[3]
            else:
                buf = player.objects_states[i[2]] == i[3]
        elif i[0] == 'f':
            if i[2] != '':
                buf = objects[obj][2]
            else:
                buf = objects[i[2]][2]
        elif i[0] == '+':
            buf = True
        elif i[0] == 'y':
            _print(*messages[i[2]], sep='\n')
            ans = _input().replace(' ', '')
            buf = ans in ('да', 'д', 'yes', 'y')
        elif i[0] == 'l':
            buf = player.location == i[2]
        elif i[0] == '>':
            buf = len(player.inventory) > 7
        elif i[0] == '$':
            buf = randint(0, 99) < i[2]
            conditions[index] = ['+', True]
        elif i[0] == 'w':
            buf = obj in i[2:]
        if i[1]:
            buf = not buf
        if not buf:
            return False
    return True
