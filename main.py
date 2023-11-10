from Engine import Engine


def main():
    engine = Engine("advmessa", "advvocab", "advobjec",
                    "advevent", "advcave", "advactio", "advclass")
    engine.save('start.json')
    while True:
        engine.events(print, input)
        input_str = [i[:4].lower() for i in input().split()]
        output = engine.input(input_str, print, input)
        if output[0] == 1:
            break
        if output[0] == 2:
            engine.save('save.json')
            break


if __name__ == "__main__":
    main()
