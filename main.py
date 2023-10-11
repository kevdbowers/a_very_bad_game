from hero import Warrior, Archer, Mage, Ranger, Spellblade, Spellbow, Hero, God

war = Warrior()
arch = Archer()
mag = Mage()
rang = Ranger()
splbld = Spellblade()
splbw = Spellbow()
hero = Hero()
cheat = God()

test_list = [war, arch, mag, rang, splbld, splbw, hero, cheat]
for x in test_list:
    print(x.name)