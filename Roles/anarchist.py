class Anarchist(Role):
    name = "Anarchist"
    alignment = "Neutral"
    species = "Human"
    categories = ["Chaos","Killing"]
    objectives = ["no-players"]
    saves = []
    tags = {"Neutral","Chaos","Killing","Human","Unique"}

    def __init__(self):
        super().__init__()
        self.actions = {"Strategically-Implemented Self-Murder" : [1, "night", Anarchist.sism], "Spanner" : [-1, "night", Anarchist.spanner], "Persuade", [2, "night", Anarchist.persuade], "Molotov", [1, "night", Anarchist.molotov]}
        self.onnightstart_abilities = [self.molotovrefresh,self.persuaderedo]
        self.persuadepeople = []
        self.molotovdone = 0

    async def sism(self, user):
        self.suicide()

    async def spanner(self, user, target):
        global Actions
        for a in [a for a in Actions if a.user == user]:
            a.fail = True

    async def persuade(self, user, target1, target2):
        target1role = target1.role
        target2role = target2.role
        target1.changerole(target2role)
        target2.changerole(target1role)
        self.persuadepeople = [target1, target1role, target2, target2role]

    async def molotov(self, user, target):
        if self.molotovdone !=0 :
            return "fail"
        target.attacked(Attack(user,1))
        self.molotovdone = 1

    async def molotovrefresh(self, user):
        if self.molotovdone == 1:
            self.molotovdone = 2
        elif self.molotovdone == 2:
            self.molotovdone = 0

    async def persuaderedo(self,user):
        if self.persuadepeople != []:
            p = self.persuadepeople
            p[0].changerole(p[1])
            p[2].changerole(p[3])
