import random
import os
import time

def drawAscii(aFileName):
    file = open(aFileName + ".txt", "r")
    image = file.read()
    print(image)
    file.close()

#Heroes
class Knight (object):
    health = 150
    strength = 15
    defence = 10
    magic = 1

class Wizard (object):
    health = 75
    strength = 5
    defence = 5
    magic = 15

class Druid (object):
    health = 125
    strength = 10
    defence = 12
    magic = 6

class Nobody (object):
    health = 100
    strength = 7
    defence = 7
    magic = 12

#Enemies
class Goblin (object):
    name = "Goblin"
    health = 30
    strength = 2
    defence = 2
    magic = 1
    loot = random.randint(0,2)

class Demon (object):
    name = "Demon"
    health = 50
    strength = 3
    defence = 4
    magic = 5
    loot = random.randint(1,4)

class Ogre (object):
    name = "Ogre"
    health = 70
    strength = 5
    defence = 6
    magic = 0
    loot = random.randint(3,5)

#Hero Selection
def heroselect ():
    print ("What are you? \n   1, 2, or 3? \n     Tell me your number\n")
    time.sleep(2)
    print("       ...You must be somebody\n")
    time.sleep(2)
    selection = input("1. Knight \n2. Wizard \n3. Druid \n\n4. Nobody.\n\n")
    if selection == "1":
        character = Knight
        print("-----------------------------\n")
        drawAscii("KnightSword")
        print ("\nThe ground shakes\n")
        return character

    elif selection == "2":
        character = Wizard
        print("-----------------------------\n")
        drawAscii("Wizard")
        print ("\nThe air charges\n")
        return character

    elif selection == "3":
        character = Druid
        drawAscii("Tree")
        print ("\nThe trees smile\n")
        return character

    elif selection == "4":
        character = Nobody
        drawAscii("TheButler")
        print ("\nThe Butler is Watching.\n")
        return character

    else:
        print ("-------\n>>select with 1, 2, or 3<<\n-------\n")
        heroselect()

def enemyselect(Goblin, Demon, Ogre):
    enemyList = [Goblin,Demon,Ogre]
    chance = random.randint(0,2)
    enemy = enemyList[chance]
    return enemy

def loot():
    loot = ["gem", "piece of meat", "clump of herbs", "mushroom", "potion"]
    lootChance = random.randint(0,4)
    lootDrop = loot[lootChance]
    return lootDrop

def battlestate():
    enemy = enemyselect(Goblin, Demon, Ogre)
    print ("-----------------------------\nOut of the darkness a", enemy.name, "rushes towards you.")
    while enemy.health > 0 :
        choice = input("-----------------------------\nWhat will you do?\n\n1. Physical Strength\n\n2. Magical Attack\n\n   3. Run\n\n")


        if choice == "1":
            print ("-----------------------------\nYou come down on the", enemy.name, "with all your might.")
            hitchance = random.randint(0, 10)
            if hitchance > 3:
                enemy.health = enemy.health - character.strength
                print("-----------------------------\nYou cleave and crush into the", enemy.name)

                if enemy.health > 0:
                    character.health = character.health - (enemy.strength / character.defence)
                    print ("-----------------------------\nthe", enemy.name, "attacks")
                    hitchance = random.randint(0,10)
                    if hitchance > 5:
                        character.health = character.health - (enemy.strength / character.defence)
                        print("-----------------------------\nthe", enemy.name, "strikes you.")
                else:
                    if enemy.name == "Goblin":
                        enemy.health = 30

                    elif enemy.name == "Demon":
                        enemy.health = 50

                    elif enemy.name == "Ogre":
                        enemy.health = 70

                    print ("-----------------------------\nThe", enemy.name, "falls.")
                    print ("It dropped something...")
                    lootDrop = loot()
                    print ("-----------------------------\nIt's a", lootDrop)
                    break
            else:
                print("-----------------------------\nYou miss.")
                print("the", enemy.name, "attacks while you're off balance and strikes you.")
                character.health = character.health - enemy.strength


character = heroselect()
battlestate()