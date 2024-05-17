acronym = ""

word = input("enter a word: ")
word_list = word.split() 

for word in word_list:
    acronym = acronym + word[0]
    
print(acronym) 
