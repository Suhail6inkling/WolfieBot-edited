class Vampires(Faction):
	name = "Vampires"
	
	class role():
		name = "Vampires"
		alignment = "Evil"
		species = "Unearthly"
		categories = ["Killing"]
		
	def __init__(self, chan):
		self.privchannel = chan
		self.actions = {"Fangs" : [-1,"night",Vampires.fangs]}
		self.members=[]
		self.onnightstart_abilities = [self.fangs_gain_use]
		self.fangsnumber = 0
		
	async def addmember(self, player):
		if player not in self.members:
			self.members.append(player)
			
	async def removemember(self, player):
		if player in self.members:
			self.members.remove(player)
	
	async def fangs(self, user, target):
	if self.fangsnumber == 0:
		if target.saves == []:
			target.changerole(Vampire())
		else:
			target.save = []
		self.fangsnumber = 1
	else:
		return "fail"
	
	async def fangs_gain_use(self, user):
		if self.fangsnumber == 1:
			self.fangsnumber = 2
		else:
			self.fangsnumber = 0
class Vampire(Role):
	name = "Vampire"
	alignment = "Evil"
	species = "Unearthly"
	categories ["Support"]
	objectives = ["evil-standard"]
	saves = []
	tags = {"Evil", "Support", "Unearthly", "Unique"}
	
	def __init__(self, vampires):
		super().__init__()
		self.actions = dict(vampires.actions)
		self.actions["Stalk"] = [1,"night",Vampire.stalk]
		self.ondaystart_abilities = [self.refresh_actions]
		self.onnightstart_abilities = [self.fangs_gain_use]
		
	async def stalk(self, user):
		#do later
