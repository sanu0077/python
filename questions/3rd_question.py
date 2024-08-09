# Q3. Grade Calculator
# Problem: Assign a letter grade based on a student's score:
# A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

number = int(input("Enter the student's number :"))

if number >=90 :
    print("Student grade is A")
elif number >=80 :
    print("student grade is B")   
elif number >=70 :
    print("student grade is c")   
elif number >=60 :
    print("student grade is d")  
else :
    print("student grade is F")          