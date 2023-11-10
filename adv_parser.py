def arg_rename(cmd_line: list, synonyms: dict):
    for index, i in enumerate(cmd_line[0]):
        if i[0] in ('o', 'a', 'h', 't', 'p', 'f'):
            if i[2] != '' and i[2] != '****':
                cmd_line[0][index][2] = synonyms[i[2][:4].lower()]
        if i[0] == 'w':
            for number, j in enumerate(i[2:]):
                cmd_line[0][index][number + 2] = synonyms[j[:4].lower()]
    for index, i in enumerate(cmd_line[1]):
        if i[0] in ('d', '*', 'c', 'a', 'n', 't'):
            if i[1] != '':
                cmd_line[1][index][1] = synonyms[i[1][:4].lower()]


def cmd_parser(in_str: str):
    data = [[], []]
    mode = 0
    count = -1
    buf = []
    for i in in_str[3:] + " ":
        match mode:
            case 0:
                if i.isspace() or i == "\n":
                    continue
                if i == "=":
                    mode = -1
                    count = -1
                    continue
                count += 1
                buf = []
                data[0].append([i])
                if i in ('%', 'y', 'l', '>', '$', 'p'):
                    mode = 1
                elif i == "+":
                    mode = 2
                elif i == "w":
                    mode = 4
                else:
                    mode = 3
            case 1:
                if i == "+":
                    data[0][count].append(False)
                elif i == "-":
                    data[0][count].append(True)
                elif i == "=":
                    data[0][count].append("".join(buf)[:4].lower())
                    buf = []
                elif i == " ":
                    data[0][count].append(int("".join(buf)))
                    mode = 0
                else:
                    buf.append(i)
            case 2:
                if i == "+":
                    data[0][count].append(False)
                    mode = 0
                elif i == "-":
                    data[0][count].append(True)
                    mode = 0
            case 3:
                if i == "+":
                    data[0][count].append(False)
                elif i == "-":
                    data[0][count].append(True)
                elif i == " ":
                    data[0][count].append("".join(buf)[:4].lower())
                    mode = 0
                else:
                    buf.append(i)
            case 4:
                if i == "+":
                    data[0][count].append(False)
                elif i == "-":
                    data[0][count].append(True)
                elif i == "(":
                    mode = 5
                elif i == " ":
                    data[0][count].append("".join(buf)[:4].lower())
                    buf = []
                    mode = 5
                else:
                    buf.append(i)
            case 5:
                if i == ")":
                    mode = 0
                elif i == " ":
                    continue
                else:
                    buf.append(i)
                    mode = 4
            case -1:
                if i.isspace() or i == "\n":
                    continue
                count += 1
                buf = []
                data[1].append([i])
                if i in ('m', 'p', 'l', '#', 't'):
                    mode = -2
                elif i == 'i':
                    mode = -3
                elif i == '"':
                    break
                else:
                    mode = -4
            case -2:
                if i == ".":
                    continue
                elif i == "=":
                    data[1][count].append("".join(buf)[:4].lower())
                    buf = []
                elif i == " ":
                    data[1][count].append(int("".join(buf)))
                    mode = -1
                else:
                    buf.append(i)
            case -3:
                if i == ".":
                    mode = -1
            case -4:
                if i == ".":
                    continue
                elif i == " " or i == "\n":
                    data[1][count].append("".join(buf)[:4].lower())
                    mode = -1
                else:
                    buf.append(i)

    return data


def evn_parser(file: str, synonyms: dict):
    init_events = []
    casual_events = []

    with open(file, "r", encoding='utf-8') as f:
        buf = []
        mode = 0
        for i in f.readlines():
            if mode == 1:
                if i[0].isspace():
                    if len(i) < 4 or i[3].isspace():
                        init_events[-1][1][-1].append(buf)
                        mode = 0
                        continue
                    buf.append(i[3:-1])
                elif i[0] == "*":
                    init_events[-1][1][-1].append(buf)
                    mode = 0
                    continue
                else:
                    init_events[-1][1][-1].append(buf)
                    mode = 0
            elif mode == 2:
                if i[0].isspace():
                    if len(i) < 4 or i[3].isspace():
                        casual_events[-1][1][-1].append(buf)
                        mode = 0
                        continue
                    buf.append(i[3:-1])
                elif i[0] == "*":
                    casual_events[-1][1][-1].append(buf)
                    mode = 0
                    continue
                else:
                    casual_events[-1][1][-1].append(buf)
                    mode = 0
            if mode == 0:
                if i[0].isspace() or i[0] == "*":
                    continue
                elif i[0] == "i":
                    buf = cmd_parser(i)
                    arg_rename(buf, synonyms)
                    init_events.append(buf)
                    if buf[1][-1][0] == '"':
                        buf = []
                        mode = 1
                elif i[0] == "e":
                    buf = cmd_parser(i)
                    arg_rename(buf, synonyms)
                    casual_events.append(buf)
                    if buf[1][-1][0] == '"':
                        buf = []
                        mode = 2
        if len(buf) > 0:
            if mode == 1:
                init_events[-1][1][-1].append(buf)
            if mode == 2:
                casual_events[-1][1][-1].append(buf)
    return init_events, casual_events


def lct_parser(file: str, synonyms: dict):
    locations = {}
    with open(file, "r", encoding='utf-8') as f:
        number = 0
        buf = []
        mode = 0
        for i in f.readlines():
            if mode == 1:
                if i[0].isspace():
                    if len(i) < 4 or i[3].isspace():
                        locations[number][2][-1][1][-1].append(buf)
                        mode = 0
                        continue
                    buf.append(i[3:-1])
                elif i[0] == "*":
                    locations[number][2][-1][1][-1].append(buf)
                    mode = 0
                    continue
                else:
                    locations[number][2][-1][1][-1].append(buf)
                    mode = 0
            if mode == 0:
                if i[0].isspace() or i[0] == "*":
                    continue
                elif i[0] == "+":
                    number = int(i[3:-1])
                    locations[number] = ["", [], []]
                elif i[0] == "s":
                    locations[number][0] = i[3:-1]
                elif i[0] == "l":
                    if i[3] != ">":
                        locations[number][1].append(i[3:-1])
                elif i[0] == "t":
                    buf = cmd_parser(i)
                    arg_rename(buf, synonyms)
                    locations[number][2].append(buf)
                    if buf[1][-1][0] == '"':
                        buf = []
                        mode = 1
    return locations


def msg_parser(file: str):
    messages = {}
    with open(file, "r", encoding='utf-8') as f:
        for i in f.readlines():
            if i[0].isspace() or i[0] == "*":
                continue
            number = int(i[:3])
            if number in messages:
                messages[number].append(i[3:-1])
            else:
                messages[number] = [i[3:-1]]
    return messages


def obj_parser(file: str, synonyms: dict[list]):
    objects = {}
    with open(file, "r", encoding='utf-8') as f:
        buf = []
        treasure = False
        for i in f.readlines():
            if i[0].isspace() or i[0] == "*":
                continue
            elif i[0] == "+":
                buf = [j[:4].lower() for j in i[3:-1].split()]
                for j in buf:
                    synonyms[j] = buf[0]
                objects[buf[0]] = ["", treasure, False, [998], 0]
            elif i[0] == "i":
                if i[3] != ">":
                    objects[buf[0]][0] = i[3:-1]
            elif i[0] == "f":
                objects[buf[0]][3] = [int(j) for j in i[3:-1].split()]
            elif i[0] == "l":
                objects[buf[0]][2] = True
                objects[buf[0]][3] = [int(j) for j in i[3:-1].split()]
            elif i[0] == "s":
                objects[buf[0]][4] = int(i[3:-1])
            elif i[0] == "=":
                treasure = True
            elif i[:3].replace(' ', '').isnumeric():
                if i[3] != ">":
                    objects[buf[0]].append(i[3:-1])
                else:
                    objects[buf[0]].append("")
    return objects


def vcb_parser(file: str):
    synonyms = {}
    trivial_answers = {}
    with open(file, "r", encoding='utf-8') as f:
        words = []
        for i in f.readlines():
            if i[0].isspace() or i[0] == "*":
                continue
            elif i[0] == "d":
                buf = [j[:4].lower() for j in i[3:-1].split()]
                for j in buf:
                    synonyms[j] = buf[0]
            elif i[0] == "s":
                words = [j[:4].lower() for j in i[3:-1].split()]
            elif i[0] == "m":
                for j in words:
                    if j in trivial_answers:
                        trivial_answers[j].append(i[3:-1])
                    else:
                        trivial_answers[j] = [i[3:-1]]
    return synonyms, trivial_answers


def act_parser(file: str,  synonyms: dict):
    actions = {}
    with open(file, "r", encoding='utf-8') as f:
        buf = []
        word = 0
        mode = 0
        for i in f.readlines():
            if mode == 1:
                if i[0].isspace():
                    if len(i) < 4 or i[3].isspace():
                        actions[word][-1][1][-1].append(buf)
                        mode = 0
                        continue
                    buf.append(i[3:-1])
                elif i[0] == "*":
                    actions[word][-1][1][-1].append(buf)
                    mode = 0
                    continue
                else:
                    actions[word][-1][1][-1].append(buf)
                    mode = 0
            if mode == 0:
                if i[0].isspace() or i[0] == "*":
                    continue
                elif i[0] == "+":
                    buf = [j[:4].lower() for j in i[3:-1].split()]
                    word = buf[0]
                    for j in buf:
                        synonyms[j] = word
                    actions[word] = []
                elif i[0] == "a":
                    buf = cmd_parser(i)
                    arg_rename(buf, synonyms)
                    actions[word].append(buf)
                    if len(buf[1]) > 0 and buf[1][-1][0] == '"':
                        buf = []
                        mode = 1
    return actions
