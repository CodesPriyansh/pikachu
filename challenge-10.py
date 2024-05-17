def subject_shortener(subj):
    sub = subj[:3]
    return sub 

def main():
    subject = input("enter your subject name: ")
    shorten_subject = subject_shortener(subject) 
    print(f"shortened subject name is {shorten_subject}") 
    
if __name__ == '__main__':
    main() 