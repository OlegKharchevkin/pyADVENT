from adv_parser import *
from db_gen import *
from cmd_processing import *
from Player import *
import json


class Engine():
    def __init__(self, messages_file: str, vocabulary_file: str, objects_file: str, events_file: str, locations_file: str, actions_file: str, scores_file: str):
        self.messages = msg_parser(messages_file)
        self.synonyms, self.trivial_answers = vcb_parser(vocabulary_file)
        self.objects = obj_parser(objects_file, self.synonyms)
        self.init_events, self.casual_events = evn_parser(
            events_file, self.synonyms)
        self.locations = lct_parser(locations_file, self.synonyms)
        self.actions = act_parser(actions_file, self.synonyms)
        objects_db = obj_db(self.objects, self.locations)
        self.scores = msg_parser(scores_file)
        objects_states = obj_states(self.objects)
        already_been = alrd_been(self.locations)
        self.player = Player([], 0, objects_db,
                             objects_states, False, already_been)

    def input(self, input_str: list, _print, _input):
        if input_str[0] in self.trivial_answers:
            _print(*self.trivial_answers[input_str[0]], sep='\n')
            return [0]
        if input_str[0] not in self.synonyms:
            _print(*self.messages[13], sep='\n')
            return [0]
        input_str = [self.synonyms[i] for i in input_str]
        input_str.append('')
        if input_str[0] in self.actions:
            for i in self.actions[input_str[0]]:
                if cnd_processing(input_str[1], i[0], self.messages, self.objects, self.player, _print, _input):
                    output = act_processing(
                        input_str[1], i[1], self.messages, self.scores, self.locations, self.objects, self.player, _print)
                    if output[0] == 0:
                        return [0]
                    if output[0] == 1:
                        return [1]
                    if output[0] == 2:
                        return [2, self.player]
                    if output[0] == 3:
                        input_str.append(output[1])
                        return self.input(input_str, _print, _input)
            else:
                _print(*self.messages[12], sep='\n')
                return [0]
        else:
            for i in self.locations[self.player.location][2]:
                if cnd_processing(input_str[0], i[0], self.messages, self.objects, self.player, _print, _input):
                    output = act_processing(
                        input_str[0], i[1], self.messages, self.scores, self.locations, self.objects, self.player, _print)
                    if output[0] == 0:
                        return [0]
                    if output[0] == 1:
                        return [1]
                    if output[0] == 2:
                        return [2, self.player]
            else:
                _print(*self.messages[12], sep='\n')
                return [0]

    def events(self, _print, _input):
        buf = []
        for i in range(len(self.init_events)):
            if cnd_processing('', self.init_events[i][0], self.messages, self.objects, self.player, _print, _input):
                output = act_processing(
                    '', self.init_events[i][1], self.messages, self.scores, self.locations, self.objects, self.player, _print)
                if output[0] == 1:
                    return [1]
                buf.append(self.init_events[i])
        for i in buf:
            self.init_events.remove(i)
        for i in range(len(self.casual_events)):
            if cnd_processing('', self.casual_events[i][0], self.messages, self.objects, self.player, _print, _input):
                output = act_processing(
                    '', self.casual_events[i][1], self.messages, self.scores, self.locations, self.objects, self.player, _print)
                if output[0] == 1:
                    return [1]

    def save(self, save_file: str):
        data = {"msgs": self.messages,
                "snnms": self.synonyms,
                "objcts": self.objects,
                "intevnts": self.init_events,
                "cslevnts": self.casual_events,
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
