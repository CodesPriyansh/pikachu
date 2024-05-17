def find_highest(num_list):
    highest = num_list[0]
    for count in range(len(num_list)):
        if num_list[count] > highest:
            highest = num_list[count] 
            
    return highest 

number_list = [1, 6, 8, 23, 55, 66, 76, 99, 34, 104]
highest_num = find_highest(number_list)
print("the highest number is", highest_num) 
