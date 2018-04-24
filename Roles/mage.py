class Mage(Role):
    name = "Mage"
    alignment = "Good"
    species = "Arcane"
    categories = ["Chaos","Investigative"]
    objectives = ["good-standard"]
    saves = []
    tags = {"Good", "Chaos","Investigative", "Arcane"}

    def __init__(self):
        super().__init__()
        self.actions = {"Switch" : [-1, "night", Mage.switch]}

    async def switch(self, user, target1, target2):
        global Actions
        if  [a for a in Actions if a.name == "Switch" and a.user != user and((a.target1 == target1 and a.target2 == target2) or (a.target1 == target2 and a.target2 == target1))] != []:
             return "fail"
        for a in [a for a in Actions if a.target == target1]:
            a.target == target2
        for a in [a for a in Actions if a.target == target2]:
            a.target == target1
        if target1.alignment == target2.alignment:
            return True
        else:
            return False
