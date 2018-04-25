class TimeLord(Role):
    name = "Time Lord"
    alignment = "Good"
    species = "Unearthly"
    categories = ["Investigative","Support"]
    objectives = [“good-standard”]
       saves = [Save(3,0,”regenerate”,self)]
    tags = {"Good","Investigative","Support","Unearthly"}

    def __init__(self):
        super().__init__()
        self.actions = {"Invite", [1, "night", TimeLord.invite], "Sonic", [1, "night", TimeLord.sonic]}

    async def invite(self, user, target):
        await ctx.invoke(self.client.get_command("tardis"),timelord=user.mention,companion=target.mention))
        target.gainmodifier(Companion())
        target.alignment == self.alignment

    async def sonic(self, user):
        rolelist = []
        #gets rolelist
        message = []
        message = x[0]
        for x in rolelist:
            if x != rolelist[0]:
                message = "{}, ".format(message)
                message = "{}{}".format(message,x)
        sonic = await ctx.invoke(self.client.get_command("sonic"),roles=message)
    
            

