user_password = input("enter your password: ")

obvious = ["password", "qwerty", "hello123", "letmein", "123456"] 

for password in obvious:
    if password == user_password:
        print("your password is weak and would be easily hacked using a brute force attack.")
    
if len(user_password) < 8:
    print("your password has failed the length check.")
else:
    print("your password has passed the length check.") 
    
char = 0
num = 0
lower = 0
upper = 0

for count in range(len(user_password)):
    if user_password[count].isdigit():
        num += 1
    elif user_password[count].isalpha():
        char += 1
        if user_password[count].isupper():
            upper += 1
        elif user_password[count].islower():
            lower += 1
            
if num == 0:
    print("you password is weak, include numkbers in it.")
if char == 0:
    print("your password is weak, include letters in it.")
if lower or upper == 0:
    print("for more security, you should include lower and upper case letters.")
if num > 0 and char > 0 and lower > 0 and upper > 0:
    print("your password meets the minimum requirements, it contains a mixture of numbers, characters and upper and lower case letters.")
    
    
