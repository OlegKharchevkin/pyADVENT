import sys
import os
import json
path = sys.argv[1]
sys.path.insert(0, path)
from adv_parser import *
from db_gen import *
from Player import *


messages_file = "./data/advmessa"
vocabulary_file = "./data/advvocab"
objects_file = "./data/advobjec"
events_file = "./data/advevent"
locations_file = "./data/advcave"
actions_file = "./data/advactio"
scores_file = "./data/advclass"
save_file = "./source/new.adv"
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
        "alrdbn": player.already_been,
        "version": "advnt.1.6"}
with open(save_file, "w", encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)
