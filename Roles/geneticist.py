class Geneticist(Role):
    name = "Geneticist"
    alignment = "Neutral"
    species = "Human"
    categories = ["Chaos","Support"]
    objectives = ["survive-end"]
    saves = []
    tags = {"Neutral","Chaos","Support","Human","Unique"}

    def __init__():
        super().__init__()
        self.actions = {"Experiment", [-1, "night", Geneticist.experiment]}

    async def experiment(self, user, target1, target2, alignment):
        twinchans = discord.utils.get(guild.channels,name="twins")
        for x in twinchans:
            if x.permissions_for(user).read_messages = True:
                return "fail"
        target1.alignment = alignment
        target2.alignment = alignment
        twinchan = await ctx.invoke(self.client.get_command("twin"),p1 = target1.mention, p2 = target2.mention)
        twin_perms = discord.PermissionOverwrite(read_messages = True)
        await twinchan.set_permissions(user, overwrite=twin_perms)
        return twinchan
