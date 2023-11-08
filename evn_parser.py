from cmd_parser import cmd_parser
from arg_rename import arg_rename


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
                        init_events[-1][1][-1] = buf
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
