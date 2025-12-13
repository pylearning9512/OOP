class Gem:
    def __init__(self,name,rank,weapon,faction,health):
        self.name=name
        self.rank=rank
        self.weapon=weapon
        self.faction=faction

        self.health=health

    def fuse(self,partner):
        
        fusion_components= {
            'opal':["amethyst", "pearl"],
            "sugulite":["amethyst","garnet"]
            }
        self.partner=partner
        
        if partner and self.name in fusion_components:
            return fusion[name]
        return f"{self.name} and {self.partner} have fused!"

    
    def attack(self,target):
        self.target=target
        if target.faction != self.faction:
            target.health= int(target.health-(10*(self.health/80)))
            if target.health<= 0:
                return f'{target.name} has been poofed!'
        else:
            print("its not nice to attack your friends :/")
        
        return (f'{self.name} attacked {target.name}!, their health is now {target.health}\n')

class Fusion(Gem):
    #in progress, need to learn about super method for classes.
    pass



pearl=Gem(
    "pearl",
    "low",
    "spear",
    "crystal gems",
    100
)

amethyst=Gem(
    "amethyst",
    "low",
    "spear",
    "crystal gems",
    150
)

ruby=Gem(
    "ruby",
    "low",
    "gaunlet",
    "crystal gems",
    30
)

sapphire=Gem(
    "sapphire",
    "low",
    "gaunlet",
    "crystal gems",
    20
)

jasper=Gem(
    "jasper",
    "high",
    "Helmet",
    "Homeworld",
    500
)


gems={
    'pearl':pearl.name,
    'amethyst':amethyst.name,
    'ruby':ruby.name,
    'sapphire':sapphire.name,
    'jasper':jasper.name}



if __name__ == '__main__':
    print("this is a module with characters, not the main file")
