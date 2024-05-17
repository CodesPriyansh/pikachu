def mean(num_list):
    total = 0
    length = len(num_list)
    for count in range(len(num_list)):
        total += num_list[count]
    
    average = total / length 
    return average

def main():
    number_list = [12, 33, 45, 56, 66, 67, 76]
    mean_out = mean(number_list)
    print("the average is", mean_out)
    
if __name__ == '__main__':
    main() 