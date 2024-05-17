cs_scores = [["karman", "45", "65","70"], ["daniel", "55", "65", "70"], 
             ["parker", "71", "78", "78"], ["jessica", "68", "79", "80"], 
             ["edie", "95", "81", "91"]] 

total = 0

for student in range(len(cs_scores)):
    for exam in range(1, 4):
        total = total + int(cs_scores[student] [exam]) 
    print("total for", cs_scores[student] [0], "=", total)
    total 
