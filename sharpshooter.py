class Sharpshooter(Role):
    name = "Sharpshooter"
    alignment = "Good"
    species = "Human"
    categories = ["Investigative", "Killing"]
    objectives = ["good-standard"]
    saves = []
    tags = {"Good", "Investigative", "Killing", "Human"}

    def __init__(self):
        super().__init__()
        self.actions = {"Scope" : [-1, "night", Sharpshooter.scope], "Snipe" : [-1, "night", Sharpshooter.snipe]}
        self.scope_results = []

    async def scope(self, user, target):
        if hasattr(user.role,"scope_results"): #No idea what this is - literally copied straight from Seer....
            user.role.scope_results[target] = [target.role.name, target.alignment]
        return [target.role.name, target.alignment]

    async def snipe(self, user, target):
        if [a for a in Actions if a.name == "Scope" and a.user == user] != []: #Literally made this up on the spot - change it to whatever
            return "fail"
        #if not used last night: (idk how to do that)
            #return "fail"
        if not hasattr(user.role, "scope_results"):
            return "fail"
        if target not in user.role.scope_results:
            return "fail"
        if target.role.name != user.role.scope_results[target][0] or target.alignment != user.role.scope_results[target][1]:
            return "fail"
        target.attacked(Attack(user,2))
