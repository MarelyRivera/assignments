#MILES PER GALLON

#ask user input for miles driven
miles = float(input("How many miles have you driven? "))
              
#ask user input for gallons used
gallons = float(input('How many gallons have you used? '))

#equation: MPG = miles driven / gallons of gas uses
mPG = miles / gallons


print("Your miles per gallon is ",format(mPG, '.2f'))


#TIP, TAX, TOTAL
#user input for charge for the food
food_charge = float(input("How much was the food? "))
#calculate the amounts of a 18% tip
tax = food_charge * 0.07
#calculate the amount for a 7% sales tax
tip = (food_charge + tax) * 0.18

total = food_charge + tax + tip

print("The tax is ", format(tax, '.2f'))
print("The tip is ", format(tip, '.2f'))
print("The total is ", format(total, '.2f'))


#Extra credit

#A = amount of money in account
#P = principal amount originally deposited
#r = annual interest rate
#n = number of times per year that interest compounds
#t = specified number of years
#equation = A = P*(1+ (r/n)) ** (n*t)

principal = float(input('How much was originally deposited? '))
rate = float(input('What is the annual interest rate? '))
compound = float(input('What is the number of times per year interest is compounded? '))
years = float(input("How many years will the account be left to earn interest? "))
balance = principal * (1+ (rate/compound)) ** (compound*years)

print(balance)
















                
