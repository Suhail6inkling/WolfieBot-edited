
def gainmodifier(self, modifier):
        self.modifiers+=modifier
        self.actions.update(modifier.actions)


async def revive(self):
        self.isAlive = True
        return "revived"
    
