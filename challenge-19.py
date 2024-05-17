import random
dice1 = 1
dice2 = 2

while dice1 != dice2:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print("dice1 rolled", dice1)
    print("dice2 rolled", dice2)
    if dice1 == dice2:
        print("game loading.")
    else: 
        again = input("press enter to roll again.") 