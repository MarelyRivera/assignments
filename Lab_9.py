
#Marely Rivera
#Lab 9
#March 31 2022

import random


#1

jupiter = {"Io":1821.6, "Europa":1560.8, "Ganymede":2634.1, "Callisto":2410.3}

moon = input("Enter the name of a Galilean moon: ")

if moon in jupiter:
    print("The mean radius is " + str(jupiter[moon]))


#2

numbers = {}
for i in range(1,101):
    num = random.randint(1,10)
    if num in numbers:
        numbers[num] += 1
    else:
        numbers[num] = 1
print(numbers)

    
# Extra Credit
text_file = open('bonus_problem.txt', 'r')
read_file = text_file.read()
word_list = read_file.split()
uniquewords = set(word_list)
text_file.close()
print(uniquewords)


        
        

