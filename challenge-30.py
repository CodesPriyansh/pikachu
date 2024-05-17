
def grade_teller(grades, desired_grade):
    for count in range(len(grades)):
        if desired_grade == grades[count] [0]:
            grade_out = grades [count] [1]
            return grade_out
        
def main():
    desired_grade = input("enter your desired grade: ") 
    user_grade = desired_grade.upper() 
    grade = grade_teller(grade_list, user_grade) 
    print("your desired grade needs these marks:", grade)



grade_list = [["A*", "90"], ["A", "83"], ["B", "72"], ["C", "60"], ["D", "49"], ["E", "30"]] 

if __name__ == '__main__':
    main() 