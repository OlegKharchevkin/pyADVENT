def obj_db(objects: dict):
    objects_db = {}
    for name, i in objects.items():
        for j in i[3]:
            if j in objects_db:
                objects_db[j].append(name)
            else:
                objects_db[j] = [name]
    return objects_db


def obj_states(objects: dict):
    objects_states = {}
    for name, i in objects.items():
        objects_states[name] = i[4]
    return objects_states
