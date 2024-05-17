def highest_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        global highest
        highest = num1 
    elif num2 > num1 and num2 > num3:
        highest = num2
    else:
        highest = num3
        
n1 = int(input("enter a number:"))
n2 = int(input("enter a number:"))
n3 = int(input("enter a number:")) 

highest_number(n1, n2, n3)

print(f"the highest number is {highest}")  
    