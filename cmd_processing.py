from Player import Player
from random import randint


def cnd_processing(obj: str, conditions: list, additional_objects: list, messages: dict, objects: dict, player: Player, _print, _input):
    for index, i in enumerate(conditions):
        buf = True
        if i[0] == 'o':
            if i[2] == '****':
                buf = obj == ''
            else:
                buf = obj == i[2]
        elif i[0] == 'h':
            if i[2] != '':
                buf = i[2] in player.objects_db[player.location] or i[2] in additional_objects
            else:
                buf = obj in player.objects_db[player.location] or obj in additional_objects
        elif i[0] == 't':
            if i[2] != '':
                buf = i[2] in player.inventory
            else:
                buf = obj in player.inventory
        elif i[0] == '%':
            buf = randint(0, 99) < i[2]
        elif i[0] == 'p':
            if i[2] == '':
                buf = player.objects_states[obj] == i[3]
            else:
                buf = player.objects_states[i[2]] == i[3]
        elif i[0] == 'f':
            if i[2] == '':
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


def act_processing(obj: str, conditions: list, additional_objects: list, actions: list, messages: dict, scores: dict, locations: dict, objects: dict, player: Player, _print, _input):
    output = [3, '']
    for i in actions:
        if i[0] == 'd':
            if i[1] == '':
                if obj in player.inventory:
                    player.inventory.remove(obj)
                if obj not in player.objects_db[player.location]:
                    player.objects_db[player.location].append(obj)
            else:
                if i[1] in player.inventory:
                    player.inventory.remove(i[1])
                if i[1] not in player.objects_db[player.location]:
                    player.objects_db[player.location].append(i[1])

        elif i[0] == '*':
            if i[1] == '':
                if obj in player.inventory:
                    player.inventory.remove(obj)
                for j in player.objects_db:
                    if obj in player.objects_db[j]:
                        player.objects_db[j].remove(obj)
            else:
                if i[1] in player.inventory:
                    player.inventory.remove(i[1])
                for j in player.objects_db:
                    if i[1] in player.objects_db[j]:
                        player.objects_db[j].remove(i[1])
        elif i[0] == 'c':
            if i[1] == '':
                if obj in player.objects_db[player.location]:
                    player.objects_db[player.location].remove(obj)
                if obj not in player.inventory:
                    player.inventory.append(obj)
            else:
                if i[1] in player.objects_db[player.location]:
                    player.objects_db[player.location].remove(i[1])
                if i[1] not in player.inventory:
                    player.inventory.append(i[1])
        elif i[0] == 'm':
            _print(*messages[i[1]], sep='\n')
        elif i[0] == 'p':
            if i[1] == '':
                player.objects_states[obj] = i[2]
            else:
                player.objects_states[i[1]] = i[2]
        elif i[0] == 'l':
            player.location = i[1]
            if player.short_ans and locations[i[1]][0] != '':
                _print(locations[i[1]][0])
            else:
                _print(*locations[i[1]][0], sep='\n')
        elif i[0] == '#':
            if i[1] == 1:
                output[0] = 1
            if i[1] == 2:
                score = player.objects_states['!bro'] * \
                    15 + player.objects_states['!see'] * 5
                for i in sorted(scores.keys(), reverse=True):
                    if score <= i:
                        _print(*score[i], sep='\n')
                        break
            if i[1] == 3:
                score = player.objects_states['!bro'] * \
                    15 + player.objects_states['!see'] * 5
                for i in sorted(scores.keys(), reverse=True):
                    if score <= i:
                        _print(*score[i], sep='\n')
                        break
                output[0] = 1
            if i[1] == 4:
                player.short_ans = True
            if i[1] == 5:
                if len(player.inventory) > 0:
                    _print(*messages[99], sep='\n')
                    for j in player.inventory:
                        _print(*objects[j][0], sep='\n')
                else:
                    _print(*messages[98], sep='\n')
            if i[1] == 6:
                _print(*locations[player.location][1], sep='\n')
                for j in player.objects_db[player.location]:
                    if objects[j][player.objects_states[j] + 5] != '':
                        _print(objects[j][player.objects_states[j] + 5])
            if i[1] == 7:
                if '!lig' not in additional_objects:
                    additional_objects.append('!lig')
                    player.objects_states['lamp'] = 1
            if i[1] == 8:
                if '!lig' in additional_objects:
                    additional_objects.remove('!lig')
                    player.objects_states['lamp'] = 0
            if i[1] == 9:
                output[0] = 2
        elif i[0] == 't':
            if i[1] == '':
                if obj in player.inventory:
                    player.inventory.remove(obj)
                for j in player.objects_db:
                    if obj in player.objects_db[j]:
                        player.objects_db[j].remove(obj)
                if obj not in player.objects_db[i[2]]:
                    player.objects_db[i[2]].append(obj)
            else:
                if i[1] in player.inventory:
                    player.inventory.remove(i[1])
                for j in player.objects_db:
                    if i[1] in player.objects_db[j]:
                        player.objects_db[j].remove(i[1])
                if i[1] not in player.objects_db[i[2]]:
                    player.objects_db[i[2]].append(i[1])
        elif i[0] == 'a':
            if i[1] == '':
                player.objects_states[obj] += 1
            else:
                player.objects_states[i[1]] += 1
        elif i[0] == 'i':
            for j in player.objects_db[player.location]:
                if objects[j][player.objects_states[j] + 5] != '':
                    _print(objects[j][player.objects_states[j] + 5])
        elif i[0] == 'n':
            output[0] = 3
            output[1] = i[1]
        elif i[0] == '"':
            _print(*i[1], sep='\n')
    return output
