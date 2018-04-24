class Sylph(Role):
    name = "Sylph"
    alignment = "Good"
    species = "Ethereal"
    categories = ["Support"]
    objectives = ["good-standard"]
    saves = []
    tags = {"Good", "Support", "Ethereal", "Unique"}

    def __init__(self):
        super().__init__()
        self.actions = {"Revitalise" : [1, "night", Sylph.revitalise]}
        self_onnightstart_abilities = [self.lunarsave]
        self_ondeath_abilities = [self.gainspectre]

    async def revitalise(self, user, target):
        if target.isAlive:
            return "fail"
        else:
            target.revive()
        return "revived"

    async def lunarsave(self, user):
        user.saves.append(Save(0,1))

    async def gainspectre(self, user):
        self.gainmodifier(Spectre())
