class Pixie(Role):
  name = "Pixie"
  alignment = "Good"
  species = "Unearthly"
  categories = ["Counteractive","Investigative"]
  objectives = ["good-standard"]
  saves = []
  tags = {"Good", "Counteractive","Investigative","Unearthly"}
  
  def __init__(self):
    super().__init__()
    self.actions = {"Flip" : [-1, "attack", Pixie.flip], "Identify" : [-1, "night", Pixie.identify]}
    #idk how to figure out number of players for this
    self.pennies = 5
    
  async def flip(self, user):
    coin = await ctx.invoke(self.client.get_command("flip"),message="1")
    if coin[0] == 1:
      global Action
      #something
      self.pennies-=1
      return ["success", self.pennies]
    self.pennies-=1
    return ["fail", self.pennies]
  
  async def identify(self, user, target):
    coin = await ctx.invoke(self.client.get_command("flip"),message="1")
    if coin[0] == 1:
      return [target.alignmennt, self.pennies]
    self.pennies-=1
    return ["fail", self.pennies]
    
    
