cs_scores = [["karman", "45", "65","70"], ["daniel", "55", "65", "70"], 
             ["parker", "71", "78", "78"], ["jessica", "68", "79", "80"], 
             ["edie", "95", "81", "91"]] 


for student in range(len(cs_scores)):
    s = 0
    for exam in range(1, 4):
        s += int(cs_scores [student] [exam])
        
        mean = s / 3
    print("average for", cs_scores[student] [0], "=", mean) 
    mean = 0
        
        
        