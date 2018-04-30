class Rogue(Role):
    name = "Rogue"
    alignment = "Good"
    species = "Human"
    categories = ["Counteractive","Protective"]
    objectives = ["good-standard"]
    saves = []
    tags = {"Good","Counteractive","Protective","Human","Unique"}

    def __init__(self):
        super().__init__()
        self.actions = {"Steal" : [-1, "night", Rogue.steal]}

    async def steal(self, user, target1, target2):
        saves = target1.saves
        target1.saves = []
        for save in saves:
            target2.saves.append(save)
