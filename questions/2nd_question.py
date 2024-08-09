# Q2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), 
# $8 for children. Everyone gets a $2 discount on Wednesday.

age = int(input("Enter your age :"))
day = str(input("Enter the day :"))

price = 12 if age >= 18 else 8

if day == "wednesday" :
    dis_price=price-2
    print("Your price is :",dis_price)
else :
    print("Price is :",price)    