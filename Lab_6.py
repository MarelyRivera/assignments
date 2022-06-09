#Excercise 1
import random

def main():

    numbers = open('numbers.txt', 'r') #open file

    for line in numbers:
        amount = float(line)     #converts text read into integer(float)
        print(amount)           #prints out the amount

         #reads the next line to be tested

    numbers.close()     #closes the file

main()


#Excercise 2: names

def main_2():
    names = open('names.txt', 'r')

    count = 0

    for line in names:
        count += 1

    print("The total number of names is: " , count, sep='')

    names.close()

main_2()

#Excercise 3: Random Numbers

def main_3():
    random_numbers = open('random_numbers.txt', 'w') #opens file
    num = int(input("How many random numbers should be created: ")) #user input

    for count in range(1,num+1):     #for loop 
        amount = random.randint(1,500)      #creates a random num
        random_numbers.write(str(amount) + '\n')    #prints the random number into the file

    random_numbers.close()   #closes the file

main_3()

#Excercise 4: Random Numbers File Reader


def main_4():

    random_numbers = open('random_numbers.txt', 'r') #open file
    count = 0
    total = 0
    
    for line in random_numbers:
        count +=1
        amount = int(line)     #converts text read into integer(float)
        total = total + amount
        print(amount)  #prints out the amount

    print("The total number of random numbers is: " , count, sep='')
    print("The total of all the numbers is: " , total, sep='')

    random_numbers.close()     #closes the file

main_4()
        
