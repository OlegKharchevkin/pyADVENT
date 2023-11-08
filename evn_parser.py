from cmd_parser import cmd_parser
from arg_rename import arg_rename


def evn_parser(file: str, synonyms: dict):
    init_events = []
    casual_events = []
    with open(file, "r", encoding='utf-8') as f:
        buf = []
        for i in f.readlines():
            if i[0].isspace() or i[0] == "*":
                continue
            elif i[0] == "i":
                buf = cmd_parser(i)
                arg_rename(buf, synonyms)
                init_events.append(buf)
            elif i[0] == "e":
                buf = cmd_parser(i)
                arg_rename(buf, synonyms)
                casual_events.append(buf)
    return init_events, casual_events
