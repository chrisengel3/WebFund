# IMPORTS 
# from _typeshed import self
import random
import os
import time

def drawAscii(aFileName):
    file = open(aFileName + ".txt", "r")
    image = file.read()
    print(image)
    file.close()

#Heroes
class Knight:
    def __init__(self):
        self.health = 150
        self.strength = 10
        self.defence = 10
        self.magic = 1
class Wizard:
    def __init__(self):
        self.health = 120
        self.strength = 5
        self.defence = 5
        self.magic = 15
class Druid:
    def __init__(self):
        self.health = 150
        self.strength = 8
        self.defence = 12
        self.magic = 6
class Nobody:
    def __init__(self):
        self.health = 100
        self.strength = 7
        self.defence = 7
        self.magic = 12


#Enemies
class Goblin:
    def __init__(self):
        self.name = "Goblin"
        self.health = 30
        self.strength = 2
        self.defence = 2
        self.magic = 1
        self.loot = random.randint(0,2)

class Demon:
    def __init__(self):
        self.name = "Demon"
        self.health = 50
        self.strength = 3
        self.defence = 4
        self.magic = 5
        self.loot = random.randint(1,4)

class Ogre:
    def __init__(self):
        self.name = "Ogre"
        self.health = 70
        self.strength = 5
        self.defence = 6
        self.magic = 0
        self.loot = random.randint(3,5)

# GAMEPLAY =======================================================

def heroselect():
    print ("What are you? \n   1, 2, or 3? \n     Tell me your number\n")
    time.sleep(2)
    print("       ...You must be somebody\n")
    time.sleep(2)
    selection = input("1. Knight \n2. Wizard \n3. Druid \n\n4. Nobody.\n\n")
    if selection == "1":
        player = Knight
        print("=" * 50)
        drawAscii("KnightSword")
        print ("\nThe ground shakes\n")
        return player

heroselect()