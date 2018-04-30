class Glazier(Role):
    name = "Glazier"
    alignment = "Good"
    species = "Human"
    categories = ["Counteractive"]
    saves =[]
    tags = {"Good","Counteractive","Human"}

    def __init__():
        super().__init__()
        self.actions = {"Reflect" : [3, "night", Glazier.reflect]}

    async def reflect(self, user):
        global Actions
        for a in [a for a in Actions if a.target == user]:
            a.target = a.user
