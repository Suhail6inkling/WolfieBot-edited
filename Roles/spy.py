class Spy(Role):
    name = "Spy"
    alignment = "Good"
    species = "Human"
    categories = ["Investigative"]
    objectives = ["good-standard"]
    saves = []
    tags = {"Good","Investigative","Human"}

    def __init__(self):
        super().__init__()
        self.actions = {"Infiltrate" : [-1, "night", Spy.infiltrate], "Surveillance" : [1, "night", Spy.surveillance]}


    async def infiltrate(self, user, target):
        priv = [target.privchan]
        if target.species == "Wolf":
            priv.append(Wolves.privchan)
        if target.role == "Bloodhound" or target.role == "Vampire":
            priv.append(Vampires.privchan)
        if target.role == "Time Lord": #and has a companion
            priv.append(self.tardis.privchan)
        for modifier in target.modifiers:
            if modifier.name == "Twin":
                priv.append(target.twin.privchan) #shrug
            if modifier.name == "Companion":
                priv.append(target.tardis.privchan)#shrug
        return [target.modifiers, priv] 
            

    async def surveillance(self, user):
        gne = [0,0,0]
        for a in Players:
            if a.alive:
                if a.alignment == "Good":
                    gne[0]+=1
                elif a.alignment == "Neutral":
                    gne[1]+=1
                else:
                    gne[2]+=1
        x = random.randint(0,2)
        y = random.randint(0,1)
        if y = 0:
            gne[x]+=1
        else:
            gne[x]-=1
        return gne
