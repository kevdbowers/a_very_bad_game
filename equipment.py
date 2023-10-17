class Stackable:  #creates class for stackable items
    def __init__(self, name, gold_value):  #constructor establishes name and value of created stackable
        self.name = name
        self.gold_value = gold_value

    def quantity(self, character):  #function for retrieving the quantity of a given stackable item
        quantity = character.stackables[self.name]
        print(f"You have {quantity} {self.name}'s remaining.")

    def pickup_stackable(self, character):  #function checking if a character can pick up and item and adjusting quantity held
        if character.stackables[self.name] < 5:
            character.stackables[self.name] += 1
        else:
            print(f"{self.name}'s are full.  You can't carry any more!")
    
    def use_potion(self, character, temp_stat):  #function for checking if a character can use a potion and then determining new stat and item quantity
        if self.name == "Healing Potion":
            if temp_stat == character.health:
                print(f"Your Health is already full!")
                return
            restored_stat = character.health

        if self.name == "Mana Potion":
            if temp_stat == character.mana:
                print(f"Your Mana is already full!")
                return
            restored_stat = character.mana

        if character.stackables[self.name] == 0:
                print(f"You have no {self.name}'s to use!")
                return
        
        character.stackables[self.name] -= 1
        recovered = int(0.5 * restored_stat)
        if temp_stat > recovered:
            temp_stat == restored_stat
            print(f"Your {self.name} fully restored you!")
        else:
            temp_stat += recovered
            print(f"Your {self.name} recovered {recovered}!")

    def use_lockpick(self, character):  #function for checking if a character can use a lockpick and then adjusting lockpick quantity
        if character.stackables[self.name] > 0:
            character.stackables[self.name] -= 1
        else:
            print(f"You have no {self.name}'s to use!")

healing_potion = Stackable("Healing Potion", 5)  #establish stackable items
mana_potion = Stackable("Mana Potion", 3)
lockpick = Stackable("Lockpick", 10)