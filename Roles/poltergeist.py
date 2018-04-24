class Poltergeist(Role):
    name = "Poltergeist"
    alignment = "Evil"
    species = "Ethereal"
    categories = ["Chaos","Investigative"]
    objectives = ["evil-standard"]
    saves = []
    tags = {"Evil", "Chaos","Investigative", "Ethereal"}

    def __init__(self):
        super().__init__()
        self.actions = {"Redirect" : [-1, "night", Poltergeist.redirect]}

    async def redirect(self, user, target1, target2):
        global Actions
        if  target1.role == user.role and ( if [a for a in Actions if a.name == "Redirect" and a.target == user] != []):
           user.suicide()
           user.gainmodifier(Spectre())
           return "fail"
        for a in target1.actions:
            target1.target = target2
        return [target1.role, target1.alignment]
