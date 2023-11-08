def cmd_parser(in_str: str):
    data = [[], []]
    mode = 0
    count = -1
    buf = []
    for i in in_str[3:] + " ":
        match mode:
            case 0:
                if i.isspace():
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
                    data[0][count].append("".join(buf)[:4])
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
                    data[0][count].append("".join(buf)[:4])
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
                    data[0][count].append("".join(buf)[:4])
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
                if i.isspace():
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
                    data[1][count].append("".join(buf)[:4])
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
                elif i == " ":
                    data[1][count].append("".join(buf)[:4])
                    mode = -1
                else:
                    buf.append(i)
    return data


if __name__ == "__main__":
    print(parser('r  o+**** a+rtrt h- t-wert %+30 p+eggs=0 f-sddf ++ y+15 l-13 >+7 $-69 w+( ghtd kjlkj jkjhuihiuhj jk ) = d. *.uhh c. m.23 p.kuujnui=5 l.76 #.3 t.hhjuiu=3 a.hjj i. n.yghuhi "'))
