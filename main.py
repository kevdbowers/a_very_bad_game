import heroes, equipment  #allows access to classes and variables from heroes.py and equipment.py

war = heroes.Warrior()
arch = heroes.Archer()
mag = heroes.Mage()
rang = heroes.Ranger()
splbld = heroes.Spellblade()
splbw = heroes.Spellbow()
hero = heroes.Hero()
cheat = heroes.God()

test_list = [war, arch, mag, rang, splbld, splbw, hero, cheat]

main_char = war
temp_health = war.health
temp_mana = war.mana

i = 0
while i < 3:
    equipment.healing_potion.quantity(war)
    equipment.healing_potion.pickup_stackable(war)

    if war.stackables["Healing Potion"] == 5:
        i += 1

i = 0
while temp_health > 0:
    equipment.healing_potion.use_potion(war, temp_health)
    temp_health -= 6 * i
    i += 1

i = 0
while i < 2:
    equipment.lockpick.quantity(war)
    equipment.lockpick.use_lockpick(war)

    if war.stackables["Lockpick"] == 0:
        i += 1

'''if isinstance(equipment.rusted_helmet, equipment.Head):
    print(equipment.rusted_helmet.armor)

print(war.equipment["head"].name)'''