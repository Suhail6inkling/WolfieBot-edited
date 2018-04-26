class StandUser(Modifier):
	name = "Stand User"
	objectives = ["stand-user"]
	tags = {"Modifier"}
	
	def __init__(self):
		super().__init__()
		self.actions - {"Battle Cry": [1, "night", StandUser.battlecry], "Stand Arrow": [1, "death", StandUser.standarrow], "Clash": [1, "night", StandUser,clash]}
	
	async def battlecry(self, user, action):
		#something
		pass
	
	async def standarrow(self, user, target):
		if "Stand User" in target.modifiers:
			target.saves.append(Save(3,2))
			target.actions["Battle Cry"][0]+=1
			target.actions["Clash"][0]+=1
		else:
			target.gainmodifier(StandUser())
	
	async def clash(self, user, target):
		if "Stand User" in target.modifiers:
			attack = target.attacked(Attack(user,2))
			if attack != "saved":
				self.actions["Battle Cry"][0]+=1
