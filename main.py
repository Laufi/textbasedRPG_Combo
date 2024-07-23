import random
#Player stats Here
PlayerAttackMin = 3
PlayerAttackMax = 5
PlayerStartHP = 20
PlayerHP = 20
PlayerBlock = 0
PlayerSpeed = 4
PlayerMagicPowerMin = 2
PlayerMagicPowerMax = 4
PlayerManaMax = 10
PlayerManaCurrent = 10

#Level stats here
PlayerLevel = 0
PlayerRequiredXP = (PlayerLevel * 5) + 5
PlayerCurrentXP = 0

#Player Equipment Here

#Player Skills Here
Craftsmanship = 0
PotionCrafting = 0
FoodPreparing = 0
FightingEfficiency = 0

#Player Resources Here
Foodstuffs = 0
Wood = 0
IronOre = 0
TitaniumOre = 0
Rope = 0

#Monster stats Here
MonsterAttackMin = 1
MonsterAttackMax = 3
MonsterHP = 5
MonsterSpeed = 3
MonsterName = "Sam"

#FloorSettings
CurrentDifficulty = 0
CurrentFloor = 0
MaxFloor = 0

#Player level calculation function
def PlayerLevelCalculation(AddedXP):
    
    global PlayerLevel
    global PlayerCurrentXP
    global PlayerRequiredXP

    PlayerXPCalculated = PlayerCurrentXP + AddedXP
    if PlayerXPCalculated >= PlayerRequiredXP:
        PlayerLevel += 1
        PlayerCurrentXP = PlayerXPCalculated - PlayerRequiredXP
        PlayerRequiredXP = PlayerRequiredXP = (PlayerLevel * 5) + 5
        print(f"You leveled up! \n Your level is now *{PlayerLevel}*! \n All of your combat stats are raised by *1*!")



#Player choice function
def PlayerChoiceFunction(MinAttack, MaxAttack, MinMagic, MaxMagic, MP):

    global MonsterHP
    global PlayerHP

    passCheck = 1 #VAR for whether or not continue loop for player choice function
    while passCheck == 1:

        PlayerChoice = input("FIGHT, MAGIC, RUN ")

        if PlayerChoice.upper() == "F" or PlayerChoice.upper() == "FIGHT":
            damage = random.randint(MinAttack, MaxAttack) #Mark damage as its own variable so can print out later
            MonsterHP -= damage
            print(f"Player Attack - EHP {MonsterHP} DMG {damage} \n")
            passCheck = 0 #DO NOT LOOP

        elif PlayerChoice.upper() == "M" or PlayerChoice.upper() == "MAGIC":
            heal = random.randint(MinMagic, MaxMagic) #Mark heal as its own variable so can print out later
            PlayerHP += heal
            print(f"Player Heal - HP {PlayerHP} HEAL {heal} \n")
            passCheck = 0 #DO NOT LOOP

        elif PlayerChoice.upper() == "R" or PlayerChoice.upper() == "RUN":
            print("You choose the easy way out.")
            exit()

        else:
            print("Wrong input") #CONTINUE LOOP
        
#Enemy Move Function
def EnemyMove(MinAttack, MaxAttack):

    global PlayerHP
    global MonsterHP

    if MonsterHP > 0: #Monster continue fight
        damage = random.randint(MinAttack, MaxAttack) #Mark damage as its own variable so can print out later
        PlayerHP -= damage
        print(f"Monster Attack - HP {PlayerHP} DMG {damage} \n")

    elif MonsterHP <= 0: #check if monster HP less than or equal to 0, win
        print("Monster has been defeated! You win! \n")
        exit()

while True:

    PlayerChoiceFunction(PlayerAttackMin, PlayerAttackMax, PlayerMagicPowerMin, PlayerMagicPowerMax, PlayerManaCurrent)

    EnemyMove(MonsterAttackMin, MonsterAttackMax)


