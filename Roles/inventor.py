class Inventor(Role):
    name = "Inventor"
    alignment = "Neutral"
    species = "Human"
    categories = ["Chaos","Killing"]
    objectives = ["last-player"]
    saves = []
    tags = {"Neutral","Chaos","Killing","Human","Unique"}

    def __init__(self):
        super().__init__()
        self.actions = {"Doomesday Device" : [-1, "night", Inventor.doomesdaydevice]}
        self.onnightstart_abilities = [self.refresh]
        self.ondaystart_abilities = [self.roleapply]
        self.doomesdayattack = 0
        self.rolechange = []

    async def doomesdaydevice(self, user):
        global Actions
        for a in [a for a in Actions if a.target == user]:
            attack = (a.user).attacked(Attack(user,2))
            if attack != "saved":
                self.doomesdayattack+=1
        if self.doomesdayattack < 2:
            user.attacked(Attack(user,2))
        else:
            global Attacks
            for a in [a for a in Attacks if a.target == user]:
                a.fail = True
                
    async def refresh(self, user):
        self.rolechange = []
        Self.doomesdayattack = 0

    async def roleapply (self, user):
        global Actions
        for a in [a for a in Actions if a.target == user and a.name == "Investigate"]:
            self.rolechange.append(Hacker())
        for a in [a for a in Actions if a.target == user and a.name == "Invite"]:
            self.rolechange.append(TARDISEngineer())
        for a in [a for a in Actions if a.target == user and a.name == "Infect"]:
            self.rolechange.append(Cyberhound())
        if len(self.rolechange)>1:
            await ctx.invoke(self.client.get_command("self.doomesdaydevice"))
        else:
            self.changerole(self.rolechange[0])
        
