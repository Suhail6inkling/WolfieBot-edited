class Priest(Role):
  name = "Priest"
  alignment = "Good"
  species = "Human"
  categories = ["Counteractive","Support"]
  objectives = ["good-standard"]
  saves = []
  tags = {"Good", "Counteractive","Support","Human","Unique"}
  
  def __init__(self):
    super().__init__()
    self.actions = {"Convert" : [1, "night", Priest.convert], "Sacrifice" : [1, "night", Priest.sacrifice], "Purify" : [1, "night", Priest.purify]}
    self.onnightstart_abilities = [self.priestcheck]
    self.ondaystart_abilities = [self.priestcheck]
  
  async def convert(self, user, target):
    target.alignment = "Good"
    
  async def sacrifice(self, user, target1, target2):
    if target2.isAlive or target1.isAlive == False:
      return "fail"
    target1.suicide()
    target2.revive()
    GoodRole = #Random good role
    target2.changerole(GoodRole)
  
  async def purify(self, user):
    for a in [a for a in players if (a.alignment == "Neutral" or a.alignment == "Evil")]:
      #Remove Saves
      pass
   
    
