def file_size(frequency, bits, duration):
    size = frequency * bits * duration
    return size 

def main():
    freq = int(input("enter the frequency in Hz: "))
    bit = int(input("enter the bit depth: ")) 
    length = int(input("enter the duration in sec: ")) 
    
    size_out = file_size(freq, bit, length) 
    size_kb = size_out / (8 * 1000) 
    size_mb = size_kb / 1000
    
    print("file size in KB:", size_kb)
    print("file size in MB", size_mb) 
    
if __name__ == '__main__':
    main() 
       
    
