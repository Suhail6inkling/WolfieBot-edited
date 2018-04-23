class Witch(Role):
    name = "Witch"
    alignment = "Neutral"
    species = "Unearthly"
    categories = ["Killing", "Protective"]
    objectives = ["witch-standard"] #Uhm, sure? - However this can change (Witch's Abilities) but idk how to
    saves = []
    tags = {"Neutral", "Killing", "Protective", "Unearthly"}

    def __init__(self):
        super().__init__()
        self.actions = {"Poison" : [-1,"night",Witch.poison], "Heal" : [-1,"night",Witch.heal]} 

    async def poison(self, user, target):
        if [a for a in Actions if a.name == "Heal" and a.target == target] != []:
            target.saves.remove(Save(0,0)) #Feel like the save needs to be removed this way - change if need be
            target.changerole(Witch())
       else:
           target.attacked(Attack(user,0))
    
    async def heal(self, user, target):
        target.saves.append(Save(0,0))
