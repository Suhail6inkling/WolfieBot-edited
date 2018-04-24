class Clockmaker(Role):
    name = "Clockmaker"
    alignment = "Neutral"
    species = "Human"
    categories = ["Chaos"]
    objectives = ["clockmaker-standard"]
    saves = []
    tags = {"Neutral","Chaos","Human"}
    
    def __init__(self):
        super().__init__()
        self.actions = {"Pendulum": [1, "night", Clockmaker.pendulum]}
        self.clock = 8
        self.strength = 0
    
    async def pendulum(self, user, target):
         attack = target.Attacked(Attack(user,self.strength))
         if attack != "saved":
             if target.alignment == "Good":
                 addition=1
             if target.alignment == "Neutral":
                 addition=1
             if target.alignment == "Evil":
                 addition=-1
             if self.clock+addition == 6:
                 self.suicide()
             if self.clock+addition == 10 or (self.clock+addition > 10 and self.clock < 10) or (self.clock+addition < 10 and self.clock > 10):
                 self.saves.append(Save(1,0))
             if self.clock+addition == 11 or (self.clock+addition > 11 and self.clock < 11) or (self.clock+addition < 11 and self.clock > 11):
                 self.strength = 2
             else:
                 self.strength = 0
             self.clock+=addition
         return self.clock
