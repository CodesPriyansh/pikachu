def vowel_counter(sentence):
    A = 0
    E = 0
    I = 0
    O = 0
    U = 0
    
    for vowel in range(len(sentence)): 
        if sentence[vowel].upper() == "A":
            A += 1 
        elif sentence[vowel].upper() == "E":
            E += 1
        elif sentence[vowel].upper() == "I":
            I += 1
        elif sentence[vowel].upper() == "O":
            O += 1
        elif sentence[vowel].upper() == "U":
            U += 1
            
    print(f"number of vowels in the sentence:- A occured {A} times, E occured {\
          E} times, I occured {I} times, O occured {O} times, U occured {O} times") 
       
sentence_in = "In the serene twilight, the golden hues of the setting sun blended seamlessly with the vibrant colors of the horizon, creating a breathtaking masterpiece that captivated all who beheld it."

vowel_counter(sentence_in) 
