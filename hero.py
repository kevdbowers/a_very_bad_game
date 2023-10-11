class Character:  #create parent class Character for class options
    def __init__(self):
        self.reputation = 0  #used for shop
        self.gold = 10
        self.inventory = []  #list to track inventory, should generally be limited to 8 slots
        self.stackables = {  #creates a dictionary to count stackable items that don't take up inventory spaces, stackables should be limited to 5 each
            "healing_potions" : 0,
            "mana_potions" : 0,
            "lockpicks" : 0
        }
        self.equipment = {  #creates slots for all equipment
            "head" : None,
            "neck" : None,
            "melee_weapon" : None,
            "off_hand" : None,
            "ranged_weapon" : None,
            "ammunition" : None,
            "ring_1" : None,
            "ring_2" : None,
            "chest" : None,
            "back" : None,
            "legs" : None,
            "feet" : None
        }

class Warrior(Character):  #create Warrior class as a Character
    def __init__(self, name = "Warrior"):  #defaults to name of class if no name is given
        self.name = name
        self.health = 20
        self.mana = 0
        self.strength = 15  #used to determine melee_damage and armor
        self.dexterity = 0  #used to determine ranged_damage and speed
        self.knowledge = 0  #used to determine magic damage and crit
        self.equipment = {}  #starting equipment

class Archer(Character):  #create Archer class as a Character
    def __init__(self, name = "Archer"):
        self.name = name
        self.health = 15
        self.mana = 0
        self.strength = 0
        self.dexterity = 15
        self.knowledge = 0
        self.equipment = {}

class Mage(Character):  #create Mage class as a Character
    def __init__(self, name = "Mage"):
        self.name = name
        self.health = 10
        self.mana = 20
        self.strength = 0
        self.dexterity = 0
        self.knowledge = 15
        self.equipment = {}

class Ranger(Character):  #create Ranger class as a Character
    def __init__(self, name = "Ranger"):
        self.name = name
        self.health = 17.5
        self.mana = 0
        self.strength = 7.5
        self.dexterity = 7.5
        self.knowledge = 0
        self.equipment = {}

class Spellblade(Character):  #create Spellblade class as a Character
    def __init__(self, name = "Spellblade"):
        self.name = name
        self.health = 15
        self.mana = 10
        self.strength = 7.5
        self.dexterity = 7.5
        self.knowledge = 0
        self.equipment = {}

class Spellbow(Character):  #create Spellbow class as a Character
    def __init__(self, name = "Spellbow"):
        self.name = name
        self.health = 12.5
        self.mana = 10
        self.strength = 0
        self.dexterity = 7.5
        self.knowledge = 7.5
        self.equipment = {}

class Hero(Character):  #create Hero class as a Character
    def __init__(self, name = "Hero"):
        self.name = name
        self.health = 15
        self.mana = 10
        self.strength = 5
        self.dexterity = 5
        self.knowledge = 5
        self.equipment = {}

class God(Character):  #create God cheat class as a Character
    def __init__(self, name = "God"):
        self.name = name
        self.health = None
        self.mana = None
        self.strength = 100
        self.dexterity = 100
        self.knowledge = 100
        self.equipment = {}