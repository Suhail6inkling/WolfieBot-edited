class Cultist(Role):
  name = "Cultist"
  alignment = "Good"
  species = "Human"
  categories = ["Counteractive","Support"]
  objectives = ["evil-standard"]
  saves = []
  tags = {"Evil", "Counteractive","Support","Human","Unique"}
  
  def __init__(self):
    super().__init__()
    self.actions = {"Convert" : [1, "night", Cultist.convert], "Sacrifice" : [1, "night", Cultist.sacrifice], "Curse" : [1, "night", Cultist.curse]}
    self.onnightstart_abilities = [self.cultistcheck]
    self.ondaystart_abilities = [self.cultistcheck]
  
  async def convert(self, user, target):
    target.alignment = "Evil"
    
  async def sacrifice(self, user, target1, target2):
    if target2.isAlive or target1.isAlive == False:
      return "fail"
    target1.suicide()
    target2.revive()
    EvilRole = #Random evil role
    target2.changerole(EvilRole)
  
  async def curse(self, user):
    for a in [a for a in players if (a.alignment == "Good")]:
      #Remove Saves
      pass

    async def cultistcheck(self, user):
    if self.alignment = "Good": #or Priest changes to Cultist
        self.changerole(Priest())
   
    
