def vowel_counter(sentence):
    vowel_list = [["A", 0], ["E", 0], ["O", 0], ["I", 0], ["U", 0]] 
    
    for count in range(len(sentence)):
        for letter in range(len(vowel_list)):
            if sentence[count].upper() == vowel_list [letter] [0] :
                vowel_list [letter] [1] = vowel_list [letter] [1] + 1
    for vowels in range(len(vowel_list)):
        print("the number of times", vowel_list [vowels] [0] , "occured is:", vowel_list [vowels] [1]) 
        
    
sentence_in = "In the serene twilight, the golden hues of the setting sun blended seamlessly with the vibrant colors of the horizon, creating a breathtaking masterpiece that captivated all who beheld it." 

vowel_counter(sentence_in)
                