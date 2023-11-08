def vcb_parser(file: str):
    synonyms = {}
    trivial_answers = {}
    with open(file, "r", encoding='utf-8') as f:
        words = []
        for i in f.readlines():
            if i[0].isspace() or i[0] == "*":
                continue
            elif i[0] == "d":
                buf = [j[:4] for j in i[3:-1].split()]
                for j in buf:
                    synonyms[j] = buf[0]
            elif i[0] == "s":
                words = [j[:4] for j in i[3:-1].split()]
            elif i[0] == "m":
                for j in words:
                    if j in trivial_answers:
                        trivial_answers[j].append(i[3:-1])
                    else:
                        trivial_answers[j] = [i[3:-1]]
    return synonyms, trivial_answers


if __name__ == "__main__":
    synonyms, trivial_answers = vcb_parser("advvocab")
    for i in sorted(synonyms.items()):
        print(i[0])
        print(i[1])
    for i in sorted(trivial_answers.items()):
        print(i[0])
        for j in i[1]:
            print(j)
