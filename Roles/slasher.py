class Slasher(Role):
    name = "Slasher"
    alignment = "Neutral"
    species = "Unearthly"
    categories = ["Chaos","Killing"]
    objectives ["last-player"]
    saves = []
    tags = {"Neutral","Chaos","Killing","Unearthly","Unique"}

    def __init__(self, user):
        super().__init++()
        self.actions = {"Slaughter" : [-1, "night", Slasher.slaughter], "Mask" : [3, "night", Slasher.mask], "Legacy" : [1, "night", Slasher.legacy]}
        self.legacytarget = ""
        self.slaughterpeople = []
        self.onndaystart_abilities = [self.slaughterattack]
        self.ondeath_abilities = [self.slasherrole]
        
    async def slaughter(self, user, target):
        target.attacked(Attack(user,1))
        slaughterer = []
        slaughterer.append(DayCount+3)
        global Actions
        for a in [a for a in Actions if a.target == user]:
            slaughterer.append(a.user)
        self.slaughterpeople.attend(slaughterer)
    async def mask(self, user):
        #something
        pass

    async def legacy(self, user, target):
        if DayCount == 1:
            self.legacyperson = target
        else:
            return "fail"

    async def slaughterattack(self, user):
        for a in self.slaugherpeople:
            if a[0] == DayCount:
                for b in a:
                    if b != a[0]:
                        b.attacked(Attack(user,0))
    async def slasherrole(self, user):
        self.legacytarget.changerole(Slasher())
        self.legacytarget.actions["Mask"][0] = 1
        self.legacytarget.actions["Legacy"][0] = 0
