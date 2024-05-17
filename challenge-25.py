import random

keeper_list = ["left", "centre", "right"] 
keeper = random.choice(keeper_list) 
keeper_score = 0
user_score = 0
for _ in range(5):
   user = input("choose: left, right, centre: ")
   if keeper == user:
       print("penalty was saved.")
       keeper_score += 1
   else:
       print("penalty was scored.") 
       user_score += 1
       
if keeper_score > user_score:
    print("keeper wins, keeper score:", keeper_score) 
else:
    print("you win, your penalty score:", user_score)
