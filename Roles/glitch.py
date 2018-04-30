class Glitch(Role):
    name = "Glitch"
    alignment = "Neutral"
    spcies = "Ethereal"
    categories = ["Chaos"]
    objectives = ["last-player"]
    saves = []
    tags = {"Neutral","Chaos","Ethereal","Unique"}

    def __init__(self, user):
        super().__init__()
        self.actions = {"Temporal Accelerator" : [1, "night", Glitch.temporalaccelerator], "Virus" : [1, "night", Glitch.virus]}
        self.virus = ""
        self.tempacc = False
        self.onnightstart_abilities =[self.virusrandom]
        self.ondaystart_abilities = [self.tempacccheck]
    
    async def temporalaccelerator(self,user):
        self.tempacc=True
        
    async def virus(self, user, target):
        self.virus = target
        global Actions
        for a in [a for a in Actions if a.user == target]:
            a.target == random.choice(players)
            
    async def tempacccheck(self, user):
        if self.tempacc:
            await game.send("A glitch has used Temporal Accelerator! This day will be skipped!")
            Day = False
            self.tempacc=False
    
    async def virusrandom(self, user):
        if self.virus.isAlive == False:
            self.virus = ""
            self.actions["Virus"][0] = 1
        global Actions
        for a in [a for a in Actions if a.user == self.virus]:
            a.target == random.choice(players)
