class Group:
    sword = "iron sword"
    armor = "dimond armor"
    group = "elf"
    def __init__(self, enchant, warior, place):
        self.place = place
        self.warior = warior
        self.enchant = enchant
class Groupp:
    sword = "dimond sword"
    armor = "iron armor"
    group = "orck"

    def __init__(self, enchant, warior, place):
        self.place = place
        self.warior = warior
        self.enchant = enchant

G1 = Group(enchant="Fire", warior=20, place="Mountain")
G2 = Groupp(enchant="Froze", warior=15, place="Near the oceon")



