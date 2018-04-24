class Dentist(Role):
    name = "Dentist"
    alignment = "Evil"
    species = "Human"
    categories = ["Counteractive"]
    objectives = ["evil-standard"]
    saves = []
    tags = {"Evil","Counteractive","Human","Unique"}

    def __init__(self):
        super().__init__()
        self.actions = {"Lockjaw" : [-1, "night", Dentist.lockjaw], "Laughing Gas" : [1, "night", Dentist.laughinggas]}
        self.onnightstart_abilities = [self.gasprep]
        self.gasperson = ""
        self.lockjawed = ""

    async def lockjaw(self, user, target):
        await ctx.invoke(self.client.get_command("lockjaw"),user=target.mention))
        self.lockjawed = target
    
    async def laughinggas(self, user, target):
        if target in self.gasperson:
            target.changerole(Jester())
        else:
            return "fail"
    
    async def gasprep(self, user):
        self.gasperson = self.lockjawed
        self.lockjawed = ""
