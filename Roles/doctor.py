class Doctor(Role):
    name = "Doctor"
    alignment = "Good"
    species = "Human"
    categories = ["Killing","Protective"]
    objectives = ["good-standard"]
    saves = []
    tags = {"Good","Killing","Protective","Human"}

    def __init__(self):
        super().__init__()
        self.actions = {"Amputate" : [-1, "night", Doctor.amputate], "Heal" : [-1, "night", Doctor.heal]}

    async def amputate(self, user, target):
        if target.alignment == "Good":
            for a in [a for a in target.saves if a.duration = 2]:
                target.saves.remove(A)
        elif target.alignment == "Neutral":
            target.attacked(Attack(user,0))
        else:
            target.Attacked(Attack(user,2))

    async def heal(self, user, target):
        target.saves.append(Save(1,0))
    
