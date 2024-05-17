import random
score = 0
for _ in range(3):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print("dice1 is rolled", dice1)
    print("dice2 is rolled" ,dice2) 
    
    total = dice1 + dice2
    print("here's the total for this round", total)
    score += total

print("your final score after 3 rounds is", score)