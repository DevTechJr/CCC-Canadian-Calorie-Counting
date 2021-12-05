burgers = [461,431,420,0]
drinks = [130,160,118,0]
sides = [100,57,70,0]
dessert = [167,266,75,0]

burgerChoice = int(input())
burgerChoice = burgers[(burgerChoice-1)]
# Sides Choice
sideChoice = int(input())
sideChoice = sides[(sideChoice-1)]
# Drink Choice
drinkChoice = int(input())
drinkChoice=drinks[(drinkChoice-1)]
# Dessert Choice
dessertChoice = int(input())
dessertChoice=dessert[(dessertChoice-1)]

print (f"Your total Calorie count is {burgerChoice+drinkChoice+sideChoice+dessertChoice}.")
