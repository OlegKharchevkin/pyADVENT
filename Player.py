class Player():
    def __init__(self, inventory: list, location: int, objects_db: dict, objects_states: dict, short_ans: bool):
        self.inventory = inventory
        self.location = location
        self.objects_db = objects_db
        self.objects_states = objects_states
        self.short_ans = short_ans
