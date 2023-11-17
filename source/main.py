"""
	Игра Collosal Cave Adventure на русском языке
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
    try:
        with open(Path("./test.test").resolve(), "w"):
            pass
        os.remove(Path("./test.test").resolve())
    except PermissionError:
        os.chdir(os.path.expanduser('~'))
    if len(sys.argv[1:]) > 0:
        for i in sys.argv[1:]:
            path = Path(i)
            if path.is_file() and path.suffix == '.adv':
                files.append(path)
    else:
        for i in Path('.').glob('*.adv'):
            files.append(i)
    print('Выберете действие:')
    print()
    print('0 Начать новую игру')
    for i in enumerate(files):
        print(f'{i[0] + 1} Загрузить {i[1]}')
    print()
    i = ''
    try:
        while True:
            i = input()
            if i.replace(' ', '').isnumeric():
                if int(i) <= len(files):
                    break
    except EOFError:
        return 2
    i = int(i)
    print()
    if i == 0:
        engine = Engine(resource_path('./new.adv'))
    else:
        engine = Engine(files[i - 1])

    while True:
        output = engine.events_processing(print, input)
        if output == 1:
            break
        try:
            while (input_str := input()).replace(' ', '') == '':
                continue
        except EOFError:
            return 2
        output = engine.input(input_str, print, input)
        if output == 1:
            break
        if output == 2:
            try:
                engine.save(f'{input("Введите имя: ")}.adv')
            except EOFError:
                return 2
            print()
            print("Готово!")
            print()
    input()
    return 0


if __name__ == "__main__":
    sys.exit(main())
