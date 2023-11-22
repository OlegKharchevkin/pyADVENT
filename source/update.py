def update(data: dict):
    version = ["advnt", "1", "5"]
    if "version" in data:
        version = [*data["version"].split(".")]
    if version[0] == "advnt":
        if version[1] == "1":
            if version[2] == "5":
                events = data["evnts"].copy()
                for i in data["evnts"]:
                    if ["a", "!bro"] in i[1]:
                        events.remove(i)
                    if ["p", False, "!bro", 17] in i[0] or ["p", False, "!bro", 16] in i[0]:
                        events[events.index(i)][0][0][2] = "!see"
                        if ["p", "!bro", 17] in i[1]:
                            events[events.index(i)][1][1][1] = "!see"
                data["evnts"] = events
                actions = data["actns"]
                synonyms = data["snnms"]
                action = []
                action.append(
                    [[["o", False, "****"]], [["m", 222]]])
                action.append(
                    [[["t", True, ""]], [["m", 14]]])
                action.append(
                    [[["l", False, 3], ["j", False, ""]], [["a", "!bro"], ["d", ""], ["m", 54]]])
                new_action = actions[synonyms["брос"]]
                new_action.remove(
                    [[["o", False, "****"]], [["m", 222]]])
                new_action.remove(
                    [[["t", True, ""]], [["m", 14]]])
                action.extend(new_action)
                actions[synonyms["брос"]] = action
                action = []
                action.append(
                    [[["h", True, ""]], [["m", 25]]])
                action.append(
                    [[["o", False, "****"]], [["m", 222]]])
                action.append(
                    [[["t", False, ""]], [["\"", ["Вы это уже несете!"]]]])
                action.append(
                    [[[">", False, 7]], [["\"", ["Вы не можете нести так много. Положите что-нибудь."]]]])
                action.append(
                    [[["l", False, 3], ["j", False, ""]], [["b", "!bro"], ["c", ""], ["m", 54]]])
                new_action = actions[synonyms["взят"]]
                new_action.remove(
                    [[["h", True, ""]], [["m", 25]]])
                new_action.remove(
                    [[["o", False, "****"]], [["m", 222]]])
                new_action.remove(
                    [[["t", False, ""]], [["\"", ["Вы это уже несете!"]]]])
                new_action.remove(
                    [[[">", False, 7]], [["\"", ["Вы не можете нести так много. Положите что-нибудь."]]]])
                action.extend(new_action)
                actions[synonyms["взят"]] = action
                action = actions[synonyms["плоф"]].copy()
                for i in action:
                    if ["p", False, "!bro", 17] in i[0] or ["p", False, "!bro", 16] in i[0]:
                        action[action.index(i)][0][1][2] = "!see"
                actions[synonyms["плоф"]] = action
                data["actns"] = actions
                action = []
                action.append(
                    [[["p", True, "!egg", 3]], [["m", 151], ["p", "!egg", 0]]])
                action.append(
                    [[["h", False, synonyms["яйца"]], ["l", False, 3]], [["p", "!egg", 0], ["t", synonyms["яйца"], 92], ["b", "!bro"], ["\"", ["Гнездо c золотыми яйцами изчезло!"]]]])
                action.append(
                    [[["h", False, "яйца"], ["l", False, 92]], [["p", "!egg", 0], ["\"", ["Гнездо c золотыми яйцами на мгновение изчезло ... и снова появилось!"]]]])
                action.append(
                    [[["h", False, "яйца"]],[["p", "!egg", 0], ["t", "яйца", 92], ["\"", ["Гнездо c золотыми яйцами изчезло!"]]]])
                action.append(
                    [[["i", False, synonyms["яйца"], 3]], [["p", "!egg", 0], ["b", "!bro"], ["t", "яйца", 92], ["\"", ["Сделано!"]]]])
                action.append(
                    [[["+", False]], [["p", "!egg", 0], ["t", "яйца", 92], ["\"", ["Сделано!"]]]])
                actions[synonyms["фук"]] = action
                data["actns"] = actions
                objects_states = data["objctsstts"]
                objects_db = data["objctsdb"]
                objects = data["objcts"]
                count = 0
                for i in objects_db["3"]:
                    if objects[i][1]:
                        count += 1
                objects_states["!bro"] = count
                data["objctsstts"] = objects_states
                version = ["advnt", "1", "6"]
                data["version"] = ".".join(version)
