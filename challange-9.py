def initials(first_name, middle_name, last_name):
    initials_out = first_name[0] + middle_name[0] + last_name[0]
    print(initials_out) 

fname = input("enter your first name: ")
mname = input("enter your middle name: ")
lname = input("enter your last name: ") 

initials(fname, mname, lname) 