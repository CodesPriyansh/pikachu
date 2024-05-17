def shopping():
    item = ''
    file = open("shopping_list.txt", "r")
    items = eval(file.read()) 
    file.close()
    while item != 'End':
        item = input("enter your shopping list items or enter 'End' to finish your list: ").title()
        
        if item != 'End':
            items.append(item)
        
    newfile = open("shopping_list.txt", "w")
    newfile.write(str(items)) 
    newfile.close() 
    
shopping() 
        
        