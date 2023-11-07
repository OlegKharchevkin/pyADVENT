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


if __name__ == "__main__":
    messages = msg_parser('advmessa')
    for i in sorted(messages.items()):
        print(i[0])
        for j in i[1]:
            print(j)
