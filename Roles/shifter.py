class Shifter(Role):
    name = "Shifter"
    alignment = "Neutral"
    species = "Ethereal"
    categories = ["Chaos"]
    objectives = []
    saves = []
    tags = {"Neutral", "Chaos","Ethereal"}
            
    def __init__(self):
        super().__init__()
        self.actions= {"Shift" : [1, "night", Shifter.shift]}

    async def shift(self, user, target):
        if target.role == user.role:
            target.suicide()
            self.suicide()
            return "suicided"
        else:
            shifterrole = user.role
            user.changerole(target.role) #shrug
            target.changerole(shifterrole) #shrug
