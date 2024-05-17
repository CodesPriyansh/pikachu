sentinel = "xxx" 
word = ""
acronym = ""

while word != sentinel:
    word = input("enter a word or xxx to finish: ")
    if word != sentinel:
        acronym = acronym + word[0] 
        
print(acronym) 