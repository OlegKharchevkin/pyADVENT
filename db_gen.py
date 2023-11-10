def obj_db(objects: dict, locations: dict):
    objects_db = {}
    for name, i in objects.items():
        for j in i[3]:
            if j in objects_db:
                objects_db[j].append(name)
            else:
                objects_db[j] = [name]
    for i in locations:
        if i not in objects_db:
            objects_db[i] = []
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
