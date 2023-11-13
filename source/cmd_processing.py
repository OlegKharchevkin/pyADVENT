"""
	Обработик команд игры Collosal Cave Adventure.
    Copyright (C) 2023  Kharchevkin Oleg (AGA)

    Этот файл — часть pyADVENT.

	pyADVENT — свободная программа: вы можете перераспространять ее и/или изменять ее на условиях
	Стандартной общественной лицензии GNU в том виде, в каком она была опубликована Фондом 
	свободного программного обеспечения; либо версии 3 лицензии, либо (по вашему выбору) любой 
	более поздней версии.

	pyADVENT распространяется в надежде, что она будет полезной, но БЕЗО ВСЯКИХ ГАРАНТИЙ; даже без 
	неявной гарантии ТОВАРНОГО ВИДА или ПРИГОДНОСТИ ДЛЯ ОПРЕДЕЛЕННЫХ ЦЕЛЕЙ. Подробнее см. в 
	Стандартной общественной лицензии GNU.

	Вы должны были получить копию Стандартной общественной лицензии GNU вместе с этой программой. 
	Если это не так, см. <https://www.gnu.org/licenses/>.
"""
from Player import Player
from random import randint


def cnd_processing(obj: str, conditions: list, messages: dict, objects: dict, player: Player, _print, _input):
    for index, i in enumerate(conditions):
        ans = True
        if len(i) >= 3:
            buf = obj if i[2] == '' else i[2]
        match i[0]:
            case 'o':
                ans = obj == ('' if i[2] == '****' else i[2])
            case 'h':
                ans = buf in player.objects_db[str(
                    player.location)] or buf in player.inventory
            case 'a':
                ans = buf in player.objects_db[str(player.location)]
            case 't':
                ans = buf in player.inventory
            case '%':
                ans = randint(0, 99) < i[2]
            case 'p':
                ans = player.objects_states[buf] == i[3]
            case 'f':
                ans = not objects[buf][2]
            case '+':
                ans = True
            case 'y':
                _print(*messages[str(i[2])], sep='\n')
                while True:
                    _print()
                    ans = _input().replace(' ', '').lower()
                    _print()
                    if ans[0] == 'д':
                        ans = True
                        break
                    if ans[0] == 'н':
                        ans = False
                        break
                    _print(*messages['994'], sep='\n')
            case 'l':
                ans = player.location == i[2]
            case '>':
                if '!lig' not in player.inventory:
                    ans = len(player.inventory) > i[2]
                else:
                    ans = len(player.inventory) > i[2] + 1
            case '$':
                ans = randint(0, 99) < i[2]
                conditions[index] = ['+', True]
            case 'w':
                ans = obj in i[2:]
        if i[1]:
            ans = not ans
        if not ans:
            return False
    return True


def act_processing(obj: str, actions: list, messages: dict, scores: dict, locations: dict, objects: dict, player: Player, _print):
    output = [0, '']
    for i in actions:
        buf = obj if i[1] == '' else i[1]
        match i[0]:
            case 'd':
                if buf in player.inventory:
                    player.inventory.remove(buf)
                for j in player.objects_db:
                    if buf in player.objects_db[j]:
                        player.objects_db[j].remove(buf)
                player.objects_db[str(player.location)].append(buf)

            case '*':
                if buf in player.inventory:
                    player.inventory.remove(buf)
                for j in player.objects_db:
                    if buf in player.objects_db[j]:
                        player.objects_db[j].remove(buf)
                player.objects_db['999'].append(buf)
            case 'c':
                if buf in player.objects_db[str(player.location)]:
                    player.objects_db[str(player.location)].remove(buf)
                if buf not in player.inventory:
                    player.inventory.append(buf)
            case 'm':
                _print(*messages[str(buf)], sep='\n')
            case 'p':
                player.objects_states[buf] = i[2]
            case 'l':
                player.location = i[1]
                if player.short_ans and locations[str(i[1])][0] != '' and player.already_been[str(i[1])]:
                    _print(locations[str(i[1])][0])
                else:
                    _print(*locations[str(i[1])][1], sep='\n')
                player.already_been[str(i[1])] = True
            case '#':
                match i[1]:
                    case 1:
                        output[0] = 1
                    case 2:
                        score = player.objects_states['!bro'] * \
                            15 + player.objects_states['!see'] * 5
                        for j in sorted(scores.keys()):
                            if score <= int(j):
                                _print(f"Счет: {score}")
                                _print(*scores[j], sep='\n')
                                break
                    case 3:
                        score = player.objects_states['!bro'] * \
                            15 + player.objects_states['!see'] * 5
                        for j in sorted(scores.keys()):
                            if score <= int(j):
                                _print(f"Счет: {score}")
                                _print(*scores[j], sep='\n')
                                break
                        output[0] = 1
                    case 4:
                        player.short_ans = True
                    case 5:
                        if len(player.inventory) > 0:
                            _print(*messages['999'], sep='\n')
                            for j in player.inventory:
                                if j != '!lig':
                                    _print('*' if objects[j][1]
                                           else ' ', objects[j][0])
                        else:
                            _print(*messages['998'], sep='\n')
                    case 6:
                        if player.already_been[str(player.location)]:
                            _print(*messages['995'], sep='\n')
                            _print()
                        _print(*locations[str(player.location)][1], sep='\n')

                        if '!lig' in player.objects_db[str(player.location)] or '!lig' in player.inventory:
                            flag = True
                            for j in player.objects_db[str(player.location)]:
                                if len(objects[j]) > player.objects_states[j] + 5 and objects[j][player.objects_states[j] + 5] != '':
                                    if flag:
                                        _print()
                                        flag = False
                                    _print(
                                        *objects[j][player.objects_states[j] + 5], sep='\n')
                    case 7:
                        if '!lig' not in player.inventory:
                            player.inventory.append('!lig')
                    case 8:
                        if '!lig' in player.inventory:
                            player.inventory.remove('!lig')
                    case 9:
                        output[0] = 2
            case 't':
                if buf in player.inventory:
                    player.inventory.remove(buf)
                for j in player.objects_db:
                    if str(buf) in player.objects_db[j]:
                        player.objects_db[j].remove(buf)
                player.objects_db[str(i[2])].append(buf)
            case 'a':
                player.objects_states[str(buf)] += 1
            case 'i':
                if '!lig' in player.objects_db[str(player.location)] or '!lig' in player.inventory:
                    for j in player.objects_db[str(player.location)]:
                        if objects[j][player.objects_states[j] + 5] != '':
                            _print(objects[j][player.objects_states[j] + 5])
            case 'n':
                output[0] = 3
                output[1] = i[1]
            case '"':
                _print(*i[1], sep='\n')
    return output
