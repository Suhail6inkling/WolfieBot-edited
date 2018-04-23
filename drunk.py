class Drunk(Role):
    name = "Drunk"
    alignment = "Neutral"
    species = "Human"
    categories = ["Chaos"]
    objectives = []
    saves = []
    tags = {"Neutral", "Chaos", "Human"}

    def __init__(self):
        super().__init__()
        self.onnightstart_abilities = [self.activesave, self.n3_changerole]
        self.ondeath_abilities = [self.spectrecheck]

    async def activesave(self, user):
        user.saves.append(Save(0,0))

    async def n3_changerole(self, user):
        if DayCount ==3 and Day == False:
            achievable = ctx.invoke(client.get_command("randomrole"), message="achievable")
            user.changerole(achievable) #or something like that

    async def spectrecheck(self, user):
        if DayCount < 3 or (DayCount ==3 and Day == True):
            self.gainmodifier(Spectre())
