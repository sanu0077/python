# Q6. Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance 
# (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).


distance = int(input("Enter the distance :"))

if distance < 3 :
    print("walk")
elif distance <16 :
    print("Bike")   
else :
    print("Car")     