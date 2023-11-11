from adv_parser import *
from db_gen import *
from cmd_processing import *
from Player import *
import json
import os

messages_file = "advmessa"
vocabulary_file = "advvocab"
objects_file = "advobjec"
events_file = "advevent"
locations_file = "advcave"
actions_file = "advactio"
scores_file = "advclass"
save_file = "new.adv"
# def parser(self, messages_file: str, vocabulary_file: str, objects_file: str, events_file: str, locations_file: str, actions_file: str, scores_file: str):
messages = msg_parser(messages_file)
synonyms, trivial_answers = vcb_parser(vocabulary_file)
objects = obj_parser(objects_file, synonyms)
events = evn_parser(events_file, synonyms)
locations = lct_parser(locations_file, synonyms)
actions = act_parser(actions_file, synonyms)
objects_db = obj_db(objects, locations)
scores = msg_parser(scores_file)
objects_states = obj_states(objects)
already_been = alrd_been(locations)
player = Player([], 0, objects_db, objects_states, False, already_been)
data = {"msgs": messages,
        "trvlanswrs": trivial_answers,
        "snnms": synonyms,
        "objcts": objects,
        "evnts": events,
        "lctns": locations,
        "actns": actions,
        "scrs": scores,
        "invntr": player.inventory,
        "lctn": player.location,
        "objctsdb": player.objects_db,
        "objctsstts": player.objects_states,
        "shrtans": player.short_ans,
        "alrdbn": player.already_been}
with open(save_file, "w", encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)
os.system('pyinstaller make.spec')
os.system('wsl pyinstaller make.spec')
