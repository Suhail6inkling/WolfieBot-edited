class Souleater(Role):
    name = "Souleater"
    alignment = "Neutral"
    species = "Ethereal"
    categories = ["Chaos","Killing"]
    objectives =["last-player"]
    saves = []
    tags = {"Neutral", "Chaos", "Killing", "Ethereal", "Achievable"}

    def __init__(self):
        super().__init()
        self.actions = {"Absorb" :[-1, "night", Souleater.absorb], "Evocation (Night)" : [-1, "night", Souleater.evocation], "Evocation (Day)" : [-1, "day", Souleater.evocation], "Consume" : [1, "night", Souleater.consume]}
        self.absorbuse = 0
        self.onnightstart_abilities = [self.absorbrefresh]
        
    async def absorb(self, user, target):
        if self.absorbuse != 0:
            return "fail"
        target.gainmodifier(Soulless())

    async def evocation(self, user, target, message):
        soulless = False
        for modifier in target.modifiers:
            if modifier.name == "Soulless":
                soulless = True
        if  not soulless:
            return "fail"
        else:
            await target.privchan.send("A Souleater has sent the following message: \n `{}`".format(message))

    async def consume(self, user, tarhet):
        soulles = False
        for modifier in target.modifiers:
            if modifier.name == "Soulless":
                soulless = True
        if not soulless:
            return "fail"
        else:
            target.suicide()
            
                
            
