#Marely Rivera
#Lab_8

#ask for a 10-character phone number
# assign numbers to letters
#.join -- puts a string back together


a = ''
numList = []

num = input("Enter a phone number in the fomrat XXX-XXX-XXXX: ")
phone = num.split('-')

print(phone)

finalList = a.join(phone)
final = finalList.upper()

print(final)

for ch in final:
    if ch.isdigit():
        ch = int(ch)
        numList.append(ch)
    elif ch.isalpha():
        if ch == 'A' or ch == 'B' or ch == 'C':
            ch = 2
            numList.append(ch)
        elif ch == 'D' or ch == 'E' or ch == 'F':
            ch = 3
            numList.append(ch)
        elif ch == 'G' or ch == 'H' or ch == 'I':
            ch = 4
            numList.append(ch)
        elif ch == 'J' or ch == 'K' or ch == 'L':
            ch = 5
            numList.append(ch)
        elif ch == 'M' or ch == 'N' or ch == 'O':
            ch = 6
            numList.append(ch)
        elif ch == 'P' or ch == 'Q' or ch == 'R' or ch == 'S':
            ch = 7
            numList.append(ch)
        elif ch == 'T' or ch == 'U' or ch == 'V':
            ch = 8
            numList.append(ch)
        elif ch == 'W' or ch == 'X' or ch == 'Y' or ch == 'Z':
            ch = 9
            numList.append(ch)

phoneNum = a.join(str(numList))

print(phoneNum)





