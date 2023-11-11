from Engine import Engine
from pathlib import Path
import sys
import os


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


def main():
    files = []
    for i in sys.argv[1:]:
        path = Path(f'.\\{i}')
        if path.is_file() and path.suffix == '.adv':
            files.append(path)
    for i in Path('.').rglob('*.adv'):
        files.append(i)
    print('Выберете действие:')
    print()
    print('0 Начать новую игру')
    for i in enumerate(files):
        print(f'{i[0] + 1} Загрузить {i[1]}')
    print()
    i = ''
    while True:
        i = input()
        if i.replace(' ', '').isnumeric():
            if int(i) <= len(files):
                break
    i = int(i)
    print()
    if i == 0:
        engine = Engine(resource_path('new.adv'))
    else:
        engine = Engine(files[i - 1])
    while True:
        output = engine.events_processing(print, input)
        if output == 1:
            break
        while (input_str := input()).replace(' ', '') == '':
            continue
        output = engine.input(input_str, print, input)
        if output == 1:
            break
        if output == 2:
            engine.save(f'{input("Введите имя: ")}.adv')
            print()
            print("Готово!")
            print()
    input()


if __name__ == "__main__":
    main()
