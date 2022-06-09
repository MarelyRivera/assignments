#2.24.22
#MARELY RIVERA

#nutritionist
# number of fat grams
# number of carbohydrate grams
        # consumed in a day
# fat calories = fat grams * 9
# carb calories = carb grams * 4

FAT_GRAMS = 9
CARB_GRAMS = 4

def main():
    fat_grams = int(input("How many fat grams do you consume per day? "))
    carb_grams = int(input("How many carb grams do you consume per day? "))

    print("The number of fat calories is: " ,fat_calories(fat_grams))
    print("The number of carb calories is: ",carb_calories(carb_grams))
    



def fat_calories(fat_grams):

    fat_cal = fat_grams * FAT_GRAMS

    return fat_cal
    

def carb_calories(carb_grams):

    carb_cal = carb_grams * CARB_GRAMS

    return carb_cal


main()


# odd even counter
# generates 100 random numbers
# counts how many are even and how many are odd
# even and odd validation

import random

def main_1():
    

    count = 0
    
    for i in range(100):
        x = random.randint(1,100)

        if (x % 2) == 0:
            count = count + 1

    print("The number of even numbers is: ", count)
    print("The number of odd numbers is: ", 100 - count)

        
    
            



main_1()


#loan payments calculator

# P = payment per month
# R = monthly interest rate as a decimal
# A = amount of loan
# M = number of months
# P = R * A / 1 - (1+R) ^ -M

def main_2():
    rate = int(input("What is the interest rate per month? " ))
    loan = int(input("What is the loan amount? "))
    months = int(input("What is the number of months? "))

    print("Your monthly payment is: ", format(payments_calc(rate,loan,months),'.2f'))



def payments_calc(rate, loan, months):

    per_rate = rate / 100

    monthly = (per_rate * loan) / (1 - (1 + per_rate) ** -months)
    
    return monthly

main_2()
            
        
        



    
    

    
