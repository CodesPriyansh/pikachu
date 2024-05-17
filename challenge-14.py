def is_odd(number):
    if int(number) % 2 == 0:
        return "even"
    else:
        return "odd"
    
def main():
    again = True
    while again:
        num = input("enter a number: ")
        if num != "stop":
            odd_out = is_odd(num) 
            print("the number is", odd_out)
        else:
            again = False
        
if __name__ == '__main__':
    main() 