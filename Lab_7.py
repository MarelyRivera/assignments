
#Lab 7
#Marely Rivera



import random

def main_1():

    num_list = []


    for i in range(8):

        number = random.randint(0,9)

        num_list.append(number)

    

    print(num_list)

main_1()




def main_2():
    nList = []

    for i in range(21):

        user_number = int(input("Enter a number: "))

        nList.append(user_number)


    minimum = min(nList)
    maximum = max(nList)
    total = sum(nList)
    average = total /len(nList)

    print('The minimum is: ', minimum)
    print('The maximum is: ', maximum)
    print('The total is: ', total)
    print('The average is: ', format(average,'.2f'))

main_2()

    
            
            
        
    

    


