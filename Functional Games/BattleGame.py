NORMAL = "normal"
POISON = "poison"
HOLY = "holy"
FIRE = "fire"


class Character:
    __slots__ = ['__name', '__hp', '__atk', '__def', '__max_hp', '__damage_type', '__poison_counter']
    def __init__(self, name, hp, atk, defence, damage_type):
        self.__name = name
        self.__hp = hp
        self.__atk = atk
        self.__def = defence
        self.__max_hp = hp
        self.__damage_type = damage_type
        self.__poison_counter = 0

    def getName(self):
        return str(self.__name)
    def getHP(self):
        return int(self.__hp)
    def getATK(self):
        return int(self.__atk)
    def getDef(self):
        return int(self.__def)
    def getMaxHP(self):
        return int(self.__max_hp)
    def getDamageType(self):
        return self.__damage_type
    def getPoisonCounter(self):
        return self.__poison_counter
    
    def setHP(self, newHP):
        self.__hp = newHP
    def setATK(self, newATK):
        self.__atk = newATK
    def setDef(self, newDef):
        self.__def = newDef
    def setPoisonCounter(self, newCounter):
        self.__poison_counter = newCounter

    #this function changes the character's Damage type
    def setDamageType(self, input):
        if (input == "poison"):
            self.__damage_type = POISON
        elif (input == "holy"):
            self.__damage_type = HOLY
        elif(input == "normal"):
            self.__damage_type = NORMAL
        elif(input == "fire"):
            self.__damage_type = FIRE
        


    def isAlive(self):
        return self.__hp > 0

    #this function will lower the character's HP, if they are dead, a message will print
    #if damage is below 0 due to high DEF, it will just deal 0 damage
    def takeDamage(self, incomingDamage, damage_type):
        damageTaken = incomingDamage - int(self.__def)

        #checks damage type and adds corresponding effect to the character
        if (damage_type == POISON):
            self.setPoisonCounter(self.__poison_counter + 2)
            damageTaken += self.__poison_counter        
        elif (damage_type == HOLY):
            self.ATKdebuf()
        elif(damage_type == FIRE):
            self.DEFdebuf()
        
        if(damageTaken < 0):
            damageTaken = 0
        newHP = self.__hp - damageTaken
        self.setHP(newHP)
        
        #prints character after all effects have been accounted for
        print(self.__name + " took " + str(damageTaken) + " points of " + str(damage_type) + " damage!")
        print(self)
        print('\n')
        if(self.__hp <= 0):
            print(self.__name + " has been slain!")
    
    #this function will heal the character for 25% of their max hp
    def heal(self):
        heal_amount = self.__max_hp / 4
        newHP = self.__hp + heal_amount
        if(newHP > self.__max_hp):
            self.setHP(self.__max_hp)
        else:
            self.setHP(newHP)

        print(self.__name + " has been healed for " + str(heal_amount) + " HP!")
        print(self)
        print('\n')

    #these add debufs to the Character's ATK and DEF, making them weaker overall
    def ATKdebuf(self):
        newATK = self.__atk - 2
        if(newATK <= 1):
            self.setATK(1)
        else:
            self.setATK(newATK)

        print(self.__name + "'s ATK has been lowered!\n")

    def DEFdebuf(self):
        newDEF = self.__def - 2
        if(newDEF <= 1):
            self.setDef(1)
        else:
            self.setDef(newDEF)

        print(self.__name + "'s DEF has been lowered!\n")
    
    #these fiunctions add buffs to the character's ATK and DEF, making them stronger
    def ATKbuff(self):
        newATK = self.__atk + 2
        self.setATK(newATK)

        print(self.__name + "'s ATK has been raised!\n")

    def DEFbuff(self):
        newDEF = self.__def + 2
        self.setDef(newDEF)

        print(self.__name +"'s DEF has been raised!\n")

    def makeChoice(self, opponent):
        choice = input(self.__name + ", Enter a command:\n\
            'attack' -> deal your ATK stat to an enemy\n\
            'type' -> change your damage type\n\
            'heal' -> Heal 25% max health\n\
            >>>\t")
        if(choice == 'heal'):
            print('\n')
            self.heal()
        elif(choice == 'type'):
            print('\n')
            damage_change = input("Change your damage type:\n\
                'poison' -> deal poison damage (increasing damage over time)\n\
                'holy' -> deal holy damage (lowers enemy ATK stat)\n\
                'fire' -> deal fire damage (lowers enemy DEF stat)\n\
                'normal' -> deal normal damage (normal damage)\n\
                >>>\t")
            if (damage_change == 'poison'):
                print('\n')
                self.setDamageType(POISON)
            elif(damage_change == 'holy'):
                print('\n')
                self.setDamageType(HOLY)
            elif(damage_change == 'fire'):
                print('\n')
                self.setDamageType(FIRE)
            else:
                print('\n')
                self.setDamageType(NORMAL)
            print(self.__name + " has changed their damage type to " + str(self.__damage_type) + "\n")
        elif(choice == 'attack'):
            opponent.takeDamage(self.__atk, self.__damage_type)
        else:
            print("Invalid Choice")

            
    #String representation of the object
    def __str__(self):
        return "Name: " + self.__name\
            + "\nHP: " + str(self.__hp) + "/" + str(self.__max_hp)\
            + "\nATK: " + str(self.__atk)\
            + "\nDEF: " + str(self.__def)\
            + "\nDamage Type: " + str(self.__damage_type) + "\n"

    
def main():
    player1Input = input("Player 1, Choose your class:\n\
        'b' -> Barbarian\n\
        'r' -> Rogue\n\
        'm' -> Mage\n\
        'p' -> Paladin\n>>>\t")
    if(player1Input == 'r'):
        player1 = Character("Rogue", 35, 7, 2, POISON)
    elif(player1Input == 'm'):
        player1 = Character("Mage", 40, 5, 4, FIRE)
    elif(player1Input == 'p'):
        player1 = Character("Paladin", 50, 6, 5, HOLY)
    else:
        player1 = Character("Barbarian", 60, 7, 6, NORMAL)

    player2Input = input("Player 2, Choose your class:\n\
        'b' -> Barbarian\n\
        'r' -> Rogue\n\
        'm' -> Mage\n\
        'p' -> Paladin\n>>>\t")
    if(player2Input == 'r'):
        player2 = Character("Rogue", 35, 7, 2, POISON)
    elif(player2Input == 'm'):
        player2 = Character("Mage", 40, 5, 4, FIRE)
    elif(player2Input == 'p'):
        player2 = Character("Paladin", 50, 6, 5, HOLY)
    else:
        player2 = Character("Barbarian", 60, 5, 6, NORMAL)
    
    while(player1.isAlive and player2.isAlive):
        player1.makeChoice(player2)
        player2.makeChoice(player1)

    

main()