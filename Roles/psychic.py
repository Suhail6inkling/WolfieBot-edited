class Psychic(Role):
    name = "Psychic"
    alignment = "Evil"
    species = "Arcane"
    categories = ["Chaos","Support"]
    saves = []
    tags = {"Evil","Chaos",Support","Arcane","Unique"}
    
    def __init__(self):
        super().__init__()
        self.actions = {"Predict" : [-1, "night", Psychic.predict], "Vessel": [-1, "night", Psychic.vessel]}
        
    async def predict(self, user, target, action):
        action = action.title()
        if action in target.actions:
            if action == "Infect":
                self.changerole(Cyberhound())
            else:
                self.actions[action] = target.actions[action]
                self.actions[action][0]=1
                if target.actions[action][0] >=1:
                    target.actions[action][0]-=1
        else:
            await target.privchan.send("A Psychic tried to guess your actions"!) #Probs not right but hey-ho
    
    async def vessel(self, user, target, action):
        action = action.title
        if action in self.actions and (action != "Predict" and action != "Vessel"):
            target.actions[action] = self.actions[action]
            del self.actions[action]
