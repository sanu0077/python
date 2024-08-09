# Q3. Grade Calculator
# Problem: Assign a letter grade based on a student's score:
# A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

number = int(input("Enter the student's number :"))
grade = 0

if (number >100 or number < 0) :
    print("Please Enter valid number")
elif number >=90 :
    print("student grade is A")    
elif number >=80 :
    print("student grade is B")   
elif number >=70 :
    print("student grade is c")   
elif number >=60 :
    print("student grade is d")  
else :
    print("student grade is F")          
    
# it can be write like this also    

# if number >100 :
#     print(" error")
# elif number >=90 :
#     grade = "B"   
# elif number >=80 :
#     grade = "C"   
# elif number >=70 :
#     grade = "D"   
# elif number >=60 :
#     grade = "E"  
# else :
#     grade = "F"     
# print("Students grade is :", grade)     