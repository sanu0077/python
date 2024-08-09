# Q1. Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).


age = int(input("Enter the age that you wants to check :"))
if age < 13 :
    print("person is child")
elif age < 20 :
    print("Teenager")
elif age < 60 :
    print("Adult")
else :
    print("Senior")
            