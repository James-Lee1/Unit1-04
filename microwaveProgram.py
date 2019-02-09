# Created by: James Lee
# Created on: Feb 2019
# Created for: ICS4U
# This program tells the user how long it will take to microwave their item of choice, given its quantity

# State variables
foodTime = 0
subTime = 1
pizzaTime = 0.75
soupTime = 1.75
userFood = ""
foodQuantity = 0

# Takes user preference of food
userFood = raw_input("Would you like to heat up a sub, pizza or soup? ")

if userFood == "sub" or userFood == "pizza" or userFood == "soup":

    foodQuantity = int(input("How many " + userFood + " would you like to heat? You can choose 1, 2 or 3. "))

    if userFood == "sub" and foodQuantity == 1:
        foodTime = subTime *1

    elif userFood == "pizza" and foodQuantity == 1:
        foodTime = pizzaTime *1

    elif userFood == "soup" and foodQuantity == 1:
        foodTime = soupTime *1

    elif userFood == "sub" and foodQuantity == 2:
        foodTime = subTime *1.5

    elif userFood == "pizza" and foodQuantity == 2:
        foodTime = pizzaTime *1.5

    elif userFood == "soup" and foodQuantity == 2:
        foodTime = soupTime *1.5

    elif userFood == "sub" and foodQuantity == 3:
        foodTime = subTime *2

    elif userFood == "pizza" and foodQuantity == 3:
        foodTime = pizzaTime *2

    elif userFood == "soup" and foodQuantity == 3:
        foodTime = soupTime *2

# Checks if food quantity is viable (between 1-3)
if foodQuantity > 3 or foodQuantity <=0:
    print("Please enter a valid input.")

else:
    print("The total time is " + str(foodTime) + " minutes")  
