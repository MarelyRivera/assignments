num = int(input("Enter a number 1-10: "))



if num >= 1 and num <= 10:
          if num == 1:
              print("I")
          elif num == 2:
              print("II")
          elif num == 3:
              print("III")
          elif num == 4:
              print("IV")
          elif num == 5:
              print("V")
          elif num == 6:
              print("VI")
          elif num == 7:
              print("VII")
          elif num == 8:
              print("VIII")
          elif num == 9:
              print("IX")
          elif num == 10:
              print("X")
else:
    print("Error")



print("Enter two of the primary colors: \nred\nblue\nyellow\n")
color_1 = str(input("Enter a primary color: "))
color_2 = str(input("Enter a primary color: "))



if color_1 == "red" and color_2 == "blue":
    print("Purple")
elif color_1 == "blue" and color_2 == "yellow":
    print("Green")
elif color_1 == "yellow" and color_2 == "red":
    print("Orange")
elif color_1 == "red" and color_2 == "yellow":
    print("Orange")
elif color_1 == "blue" and color_2 == "red":
    print("Purple")
elif color_1 == "yellow" and color_2 == "blue":
    print("Green")
else:
    print("Error")
