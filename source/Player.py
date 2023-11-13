"""
	Класс персонажа игры Collosal Cave Adventure на русском языке
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


class Player():
    def __init__(self, inventory: list, location: int, objects_db: dict, objects_states: dict, short_ans: bool, already_been: dict):
        self.inventory = inventory
        self.location = location
        self.objects_db = objects_db
        self.objects_states = objects_states
        self.short_ans = short_ans
        self.already_been = already_been
