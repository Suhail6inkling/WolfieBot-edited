class Whisperer(Role):
    name = "Whisperer"
    alignment = "Good"
    species = "Arcane"
    categories = ["Investigative","Support"]
    objectives = ["good-standard"]
    saves = []
    tags = {"Good","Investigative","Support","Arcane","Unique"}

    def __init__(self):
        super().__init__()
        self.actions = {"Whisper" : [-1, "night", Whisperer.whisper]}
        self.ondeathactions = [self.spectregain]

    async def whisper(self, user, role, message):
        whisperers = []
        role = role.title()
        if role = "Rojinbi":
            role = "Rōjinbi"
        if role = "Tardis Engineer":
            role = "TARDIS Engineer"
        for a in players:
            if a.role.name == role:
                whisperers.append(a)
        if whisperers = []:
            return "noone"
            self.actions["Whisper"][0] = 0
        for a in whisperers:
            await a.chan.send("A Whisperer has sent you the following message: `{}`".format(message))
        
    async def spectregain(self, user):
        if Day == False:
            self.gainmodifier(Spectre())
