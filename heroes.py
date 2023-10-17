class Character:  #create parent class Character for class options
    def __init__(self, reputation, gold, inventory):
        self.reputation = reputation  #used for shop
        self.gold = gold
        self.inventory = inventory  #list to track inventory, should generally be limited to 8 slots

class Warrior(Character):  #create Warrior class as a Character
    def __init__(self, reputation = 0, gold = 10, inventory = [], name = "Warrior"):  #defaults to name of class if no name is given
        self.name = name
        self.health = 20
        self.mana = 0
        self.armor_class = 4
        self.strength = 15  #used to determine melee_damage and armor
        self.dexterity = 0  #used to determine ranged_damage and speed
        self.knowledge = 0  #used to determine magic damage and crit
        self.stackables = {  #creates a dictionary to count stackable items that don't take up inventory spaces, stackables should be limited to 5 each
            "Healing Potion" : 3,
            "Mana Potion" : 0,
            "Lockpick" : 1
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
            "gloves" : None,
            "chest" : None,
            "back" : None,
            "legs" : None,
            "feet" : None
        }
        super().__init__(reputation, gold, inventory)

class Archer(Character):  #create Archer class as a Character
    def __init__(self, reputation = 0, gold = 10, inventory = [], name = "Archer"):
        self.name = name
        self.health = 15
        self.mana = 0
        self.armor_class = 2
        self.strength = 0
        self.dexterity = 15
        self.knowledge = 0
        self.stackables = {  #creates a dictionary to count stackable items that don't take up inventory spaces, stackables should be limited to 5 each
            "Healing Potion" : 3,
            "Mana Potion" : 0,
            "Lockpick" : 1
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
            "gloves" : None,
            "chest" : None,
            "back" : None,
            "legs" : None,
            "feet" : None
        }
        super().__init__(reputation, gold, inventory)

class Mage(Character):  #create Mage class as a Character
    def __init__(self, reputation = 0, gold = 10, inventory = [], name = "Mage"):
        self.name = name
        self.health = 10
        self.mana = 20
        self.armor_class = 1
        self.strength = 0
        self.dexterity = 0
        self.knowledge = 15
        self.stackables = {  #creates a dictionary to count stackable items that don't take up inventory spaces, stackables should be limited to 5 each
            "Healing Potion" : 2,
            "Mana Potion" : 1,
            "Lockpick" : 1
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
            "gloves" : None,
            "chest" : None,
            "back" : None,
            "legs" : None,
            "feet" : None
        }
        super().__init__(reputation, gold, inventory)

class Ranger(Character):  #create Ranger class as a Character
    def __init__(self, reputation = 0, gold = 10, inventory = [], name = "Ranger"):
        self.name = name
        self.health = 17.5
        self.mana = 0
        self.armor_class = 3
        self.strength = 7.5
        self.dexterity = 7.5
        self.knowledge = 0
        self.stackables = {  #creates a dictionary to count stackable items that don't take up inventory spaces, stackables should be limited to 5 each
            "Healing Potion" : 3,
            "Mana Potion" : 0,
            "Lockpick" : 1
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
            "gloves" : None,
            "chest" : None,
            "back" : None,
            "legs" : None,
            "feet" : None
        }
        super().__init__(reputation, gold, inventory)

class Spellblade(Character):  #create Spellblade class as a Character
    def __init__(self, reputation = 0, gold = 10, inventory = [], name = "Spellblade"):
        self.name = name
        self.health = 15
        self.mana = 10
        self.armor_class = 2
        self.strength = 7.5
        self.dexterity = 7.5
        self.knowledge = 0
        self.stackables = {  #creates a dictionary to count stackable items that don't take up inventory spaces, stackables should be limited to 5 each
            "Healing Potion" : 2,
            "Mana Potion" : 1,
            "Lockpick" : 1
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
            "gloves" : None,
            "chest" : None,
            "back" : None,
            "legs" : None,
            "feet" : None
        }
        super().__init__(reputation, gold, inventory)

class Spellbow(Character):  #create Spellbow class as a Character
    def __init__(self, reputation = 0, gold = 10, inventory = [], name = "Spellbow"):
        self.name = name
        self.health = 12.5
        self.mana = 10
        self.armor_class = 2
        self.strength = 0
        self.dexterity = 7.5
        self.knowledge = 7.5
        self.stackables = {  #creates a dictionary to count stackable items that don't take up inventory spaces, stackables should be limited to 5 each
            "Healing Potion" : 2,
            "Mana Potion" : 1,
            "Lockpick" : 1
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
            "gloves" : None,
            "chest" : None,
            "back" : None,
            "legs" : None,
            "feet" : None
        }
        super().__init__(reputation, gold, inventory)

class Hero(Character):  #create Hero class as a Character
    def __init__(self, reputation = 0, gold = 10, inventory = [], name = "Hero"):
        self.name = name
        self.health = 15
        self.mana = 10
        self.armor_class = 3
        self.strength = 5
        self.dexterity = 5
        self.knowledge = 5
        self.stackables = {  #creates a dictionary to count stackable items that don't take up inventory spaces, stackables should be limited to 5 each
            "Healing Potion" : 2,
            "Mana Potion" : 1,
            "Lockpick" : 1
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
            "gloves" : None,
            "chest" : None,
            "back" : None,
            "legs" : None,
            "feet" : None
        }
        super().__init__(reputation, gold, inventory)

class God(Character):  #create God cheat class as a Character
    def __init__(self, reputation = 1000, gold = 10000, inventory = [], name = "God"):
        self.name = name
        self.health = None
        self.mana = None
        self.armor_class = 5
        self.strength = 100
        self.dexterity = 100
        self.knowledge = 100
        self.stackables = {  #creates a dictionary to count stackable items that don't take up inventory spaces, stackables should be limited to 5 each
            "Healing Potion" : 6,
            "Mana Potion" : 6,
            "Lockpick" : 6
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
            "gloves" : None,
            "chest" : None,
            "back" : None,
            "legs" : None,
            "feet" : None
        }
        super().__init__(reputation, gold, inventory)