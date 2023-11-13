"""
	Движок игры Collosal Cave Adventure на русском языке
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
from cmd_processing import *
from Player import *
import json


class Engine():
    def __init__(self, save_file: str):
        with open(save_file, "r", encoding='utf-8') as f:
            data = json.load(f)
        self.messages = data["msgs"]
        self.trivial_answers = data["trvlanswrs"]
        self.synonyms = data["snnms"]
        self.objects = data["objcts"]
        self.events = data["evnts"]
        self.locations = data["lctns"]
        self.actions = data["actns"]
        self.scores = data["scrs"]
        self.player = Player(data["invntr"], data["lctn"],
                             data["objctsdb"], data["objctsstts"], data["shrtans"], data["alrdbn"])

    def input(self, input_str: str, _print, _input):
        _print()
        input_str = [i[:4].lower() for i in input_str.split()]
        buf = [i not in self.synonyms for i in input_str]
        output = [0]
        if True in buf:
            _print(*self.messages['997'], sep='\n')
        elif (input_str := [self.synonyms[i] for i in input_str])[0] in self.trivial_answers:
            _print(*self.trivial_answers[input_str[0]], sep='\n')
        elif input_str[0] in self.actions:
            input_str.append('')
            for i in self.actions[input_str[0]]:
                if cnd_processing(input_str[1], i[0], self.messages, self.objects, self.player, _print, _input):
                    output = act_processing(
                        input_str[1], i[1], self.messages, self.scores, self.locations, self.objects, self.player, _print)
                    if output[0] == 3:
                        input_str[1] = output[1]
                        for i in self.actions[input_str[0]]:
                            if cnd_processing(input_str[1], i[0], self.messages, self.objects, self.player, _print, _input):
                                output = act_processing(
                                    input_str[1], i[1], self.messages, self.scores, self.locations, self.objects, self.player, _print)
                                break
                    break
            else:
                _print(*self.messages['996'], sep='\n')
        else:
            for i in self.locations[str(self.player.location)][2]:
                if cnd_processing(input_str[0], i[0], self.messages, self.objects, self.player, _print, _input):
                    output = act_processing(
                        input_str[0], i[1], self.messages, self.scores, self.locations, self.objects, self.player, _print)
                    break
            else:
                _print(*self.messages['996'], sep='\n')
        _print()
        return output[0]

    def events_processing(self, _print, _input):
        global gflag
        gflag = False
        output = [0]
        for i in range(len(self.events)):
            if cnd_processing('', self.events[i][0], self.messages, self.objects, self.player, _print, _input):
                def _print_with_flag(*args, **kwargs):
                    _print(*args, **kwargs)
                    global gflag
                    gflag = True
                output = act_processing(
                    '', self.events[i][1], self.messages, self.scores, self.locations, self.objects, self.player, _print_with_flag)
                if output[0] == 1:
                    break
        if gflag:
            _print()
        return output[0]

    def save(self, save_file: str):
        data = {"msgs": self.messages,
                "trvlanswrs": self.trivial_answers,
                "snnms": self.synonyms,
                "objcts": self.objects,
                "evnts": self.events,
                "lctns": self.locations,
                "actns": self.actions,
                "scrs": self.scores,
                "invntr": self.player.inventory,
                "lctn": self.player.location,
                "objctsdb": self.player.objects_db,
                "objctsstts": self.player.objects_states,
                "shrtans": self.player.short_ans,
                "alrdbn": self.player.already_been}
        with open(save_file, "w", encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)
