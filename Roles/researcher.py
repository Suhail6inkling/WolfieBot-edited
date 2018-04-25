class Researcher(Role):
    name = "Researcher"
    alignment = "Good"
    species = "Human"
    categories = ["Investigative"]
    objectives = ["good-standard"]
    saves = []
    tavs = {"Good","Investigative","Human"}

    def __init__(self):
        super().__init__()
        self.actions = {"Research" : [-1, "night", Researcher.research]}
        
    async def research(self, user, target):
        global Actions
        people = []
        for a in [a for a in Actions if a.target == target]:
            people = "{} {}".format(people,a.user.mention)
        return people
    
            
