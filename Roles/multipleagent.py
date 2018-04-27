class MultipleAgent(Role):
    name = "Multiple Agent"
    alignment = "Neutral"
    species = "Human"
    categories = ["Chaos","Protective"]
    objectives = []
    saves = []
    tags = {"Neutral","Chaos","Protective","Human"}

    def __init__(self):
        super().__init__()
        self.actions = {"Loyalty" : [-1, "night", MultipleAgent.loyalty], "Heal" : [1, "night", MultipleAgent.heal]}
        self.streak=[0,""]
        self.ondaystart_abilties = [self.loyaltycheck]
        self.onnightstart_abilities=[self.loyaltyundo]
            
    async def loyalty(self, user, target):
        self.alignment = target.alignment
        self.objectives = target.objectives
        if target.alignment=self.streak[1]:
            self.streak[0]+=1
        else:
            self.streak = [1, target.alignment]
        if self.streak = [3,"Good"]:
            self.changerole(Spy())
        if self.streak = [3,"Evil"]:
            self.changerole(Psychic())

    async def heal(self, user, target):
        if target.alignment == self.alignment:
            target.saves.append(Save(0,0))

    async def loyaltycheck(self, user):
        if self.alignment == "Neutral":
            target = random.choice(Players)
            self.loyalty(self, user, target)

    async def loyaltyundo(self, user):
        self.alignment == "Neutral"
        self.objectives = []
