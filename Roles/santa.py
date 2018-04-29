class  Santa(Role):
    name = "Santa"
    alignment = "Neutral"
    species = "Unearthly"
    categories = ["Support"]
    objectives = ["santa-standard"]
    saves = []
    tags = {"Neutral","Support","Unearthky","Unique"}

    def __init__(self):
        super().__init__()
        self.actiions = {"Gift" : [-1, "night", Santa.gift], "Coal" : [0, "night", Santa.coal]}
        self.onnightstart_abilities = [self.caneorcoal]
        self.gifted = ""

    async def gift(self, user, target):
        self.gifted = target

    async def coal(self, user, target):
        if target.role == "Santa":
            return "fail"
        target.attacked(Attack(user, 2))

    async def caneorcoal(self, user):
        #get lynched player
        if lynched.alignment != self.gifted.alignment:
            self.gifted.saves.append(Save(0,3))
            self.saves.append(Save(0,3))
            self.gifted = ""
            return "candy cane"
        else:
            self.gifted.actions["Coal"] = self.actions["Coal"]
            self.gifted.actions["Coal"][0] = 1
            

