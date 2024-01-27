class Group:
    sword = "iron sword"
    armor = "dimond armor"
    group = "elf"
    def __init__(self, enchant, warior, place):
        self.place = place
        self.warior = warior
        self.enchant = enchant
class Groupp:
    skin = "Aura"
    item = "tea"
    planet = "Mars"

    def __init__(self, name, house, brother):
        self.name = name
        self.house = house
        self.brother = brother

G1 = Group(enchant="Fire", warior=20, place="Mountain")
G2 = Groupp(name="Yura", house=13, brother="2 brother")

print(G2.brother)
print(G2.item)
