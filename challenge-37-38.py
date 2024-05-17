def generate_username(first_name, last_name):
    
    username = last_name + first_name[0] 
    
    users_file = open("users.txt", "r")
    usernames = eval(users_file.read()) 
    users_file.close() 
    
    for count in range(len(usernames)):
        if usernames[count] [0] == username:
            username = username + "#"
    print("your username is", username)

fname = input("enter your first name: ") 
lname = input("enter your last name: ") 
    
generate_username(fname, lname)       
 

