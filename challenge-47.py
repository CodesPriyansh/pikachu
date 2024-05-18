#Q1 
def text_size(bits_char, num_char):
    size = bits_char * num_char
    return size

#Q2 8000 bita

#Q4 more characters can be represented using unicode(2^32) like emojis and non-english characters e.g. japanese.

#Q4 
def main(bits_char, num_char):
    size = bits_char * num_char
    size_kb = size / (8 * 1000)
    print(size_kb) 
    
main() 

#Q5 - 1KB