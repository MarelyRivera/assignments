# Marely Rivera
# Lab 4
# 2.17.2022

# Distance Traveled
speed = int(input("What is the speed of the vehicle in miles per hour? "))
hours = int(input("How many hours has the vehicles traveled? "))




print("Hour" , '\t' , "Distance Traveled")


for i in range(hours + 1):
    
    distance = speed * i
    
    print(i , '\t', distance)


#Pennies for Pay


days = int(input("Enter a number of days: "))

total = 0

print("Days", '\t' , "Salary")

for x in range(1, days+1):
    salary = 2**(x-1)*0.01
    print(x, '\t', salary)
    total = total + salary

print("Total", '\t', format(total, ',.2f'))
    
    
   
    
