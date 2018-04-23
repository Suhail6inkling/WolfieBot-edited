class Noir(Role):
    name = "Noir"
    alignment = "Good"
    species = "Human"
    categories = ["Investigative","Killing"]
    objectives = ["good-standard"]
    saves = []
    tags = {"Good", "Investigative","Killing", "Human", "Unique"}

    def __init__(self):
        super().__init__()
        self.actions = {"Interrogate" : [-1, "night", Noir.interrogate]}

    async def interrogate(self, user, target, category):
        if category in target.categories:
            target.attacked(Attack(user,0))
        return [target.categories]
