def obj_parser(file: str, synonyms: dict[list]):
    objects = {}
    with open(file, "r", encoding='utf-8') as f:
        buf = []
        treasure = False
        for i in f.readlines():
            if i[0].isspace() or i[0] == "*":
                continue
            elif i[0] == "+":
                buf = [j[:4] for j in i[3:-1].split()]
                for j in buf:
                    synonyms[j] = buf
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


if __name__ == "__main__":
    synonyms = {}
    objects = obj_parser("advobjec", synonyms)
    for i in sorted(objects.items()):
        print(i[0])
        print(i[1])
