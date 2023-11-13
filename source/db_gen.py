"""
	Генератор баз данных игры Collosal Cave Adventure.
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


def obj_db(objects: dict, locations: dict):
    objects_db = {}
    for name, i in objects.items():
        for j in i[3]:
            if str(j) in objects_db:
                objects_db[str(j)].append(name)
            else:
                objects_db[str(j)] = [name]
    for i in locations:
        if str(i) not in objects_db:
            objects_db[str(i)] = []
    return objects_db


def obj_states(objects: dict):
    objects_states = {}
    for name, i in objects.items():
        objects_states[name] = i[4]
    return objects_states


def alrd_been(locations: dict):
    already_been = {}
    for i in locations:
        already_been[i] = False
    return already_been
