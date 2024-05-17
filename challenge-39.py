def new_user(username_in, password_in):
    file = open("users.txt", "r") 
    users = eval(file.read()) 
    file.close() 
    
    new_user = [] 
    
    new_user.append(username_in)
    new_user.append(password_in)
    
    users.append(new_user) 
    
    users_file = open("users.txt", "w")
    users_file.write(str(users)) 
    users_file.close() 
    
username = input("enter your username: ")
password = input("enter your password: ")

new_user(username, password) 

