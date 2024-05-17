def options(num):
    if num == 1:
        return "Computer Science"
    elif num == 2:
        return "Music"
    elif num == 3:
        return "Dance"
    elif num == 4:
        return "PE"
    else:
        return "Error"
        
def main():
    print('''
          1. Computer Science
          2. Music
          3. Dance
          4. PE
          ''') 
          
          
    option_num = int(input("enter your subject number: ")) 
    subject = options(option_num)
    if subject == "Error":
        print("your input is invalid.")
        print("enter a number between 1 and 4.")
        return main()
        
    else:  
        print("you chose", subject) 
        
        
main()  

