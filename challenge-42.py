def hex_to_denary(hex_in):
    A_TO_F = [["A", "10"], ["B", "11"], ["C", "12"], ["D", "13"], ["E", "14"], ["F", "15"]] 
    
    convert = False
    
    for count in range(len(A_TO_F)):
        if hex_in == A_TO_F [count] [0]:
            convert = True 
            return A_TO_F [count] [1]
        
    if convert == False:
        return int(hex_in) 
    
def main():
    hex_i = input("enter the digit: ") 
    hex_out = hex_to_denary(hex_i) 
    print(hex_out) 
    
main() 
        