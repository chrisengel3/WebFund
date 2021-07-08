import random
import os
import time

def drawAscii(aFileName):
    file = open(os.path.join(os.path.dirname(os.path.realpath(__file__)),aFileName + ".txt"), "r")
    image = file.read()
    print(image)
    file.close()
    
#Heroes
class Pirate:
    def __init__(self):
        self.health = 150
        self.strength = 10
        self.defence = 10
        self.magic = 1
        self.loot = random.randint(3,5)

    def rum_rage(self , Ninja):
        self.health -= 5
        self.strength += 7
        Ninja.health -= self.strength
        return self
    
    def sword_slice(self , Ninja):
        Ninja.health -= self.strength
        return self
    
    def pistol_whip(self , Ninja):
        Ninja.health -= self.strength
        return self

    def parrots_might(self , Ninja):
        Ninja.health -= self.strength
        return self

    def wooden_leg_melee(self , Ninja):
        Ninja.health -= self.strength
        # self.
        return self

class Ninja:
    def __init__(self):
        self.health = 120
        self.strength = 5
        self.defence = 5
        self.magic = 15
        self.loot = random.randint(3,5)

    def attack( self, Pirate):
        Pirate.health -= self.strength
        return self

    #     def concentrate( self, Pirate):
    #     self.health += 30
    #     return self

    # def ninja_star(self, Pirate):
    #     Pirate.health -= 10
    #     return self
        
    # # def 


# GAMEPLAY =======================================================

def heroselect():
    print ("What are you? \n   1, 2, or 3? \n     Tell me your number\n")
    time.sleep(2)
    print("       ...You must be somebody\n")
    time.sleep(2)
    selection = input("1. Pirate \n2. Ninja \n3. Druid \n\n4. Nobody.\n\n")
    if selection == "1":
        player = Pirate
        print("=" * 50)
        drawAscii("KnightSword")
        print ("\nThe ground shakes\n")
        return player
        
    elif selection == "2":
        player = Ninja
        print("=" * 50)
        drawAscii("KnightSword")
        print ("\nThe ground shakes\n")
        return player

heroselect()