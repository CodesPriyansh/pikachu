def is_multiple(x_in, y_in):
    if x_in % y_in == 0:
        print(x_in, "is a multiple of", y_in)
    else:
        print(x_in, "is not a multiple of", y_in)
    
x = int(input("enter a number: ")) 
y = int(input("enter a number: ")) 

is_multiple(x, y) 