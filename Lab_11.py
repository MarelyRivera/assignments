MI_TO_M = 1609.34

#1
TIME = 120

#2
initial_velocity = float(input("What's your initial velocity? "))
time = float(input('How much time elapsed? '))
acceleration = float(input('You were travelling at what acceleration? '))

#3
vConvert = initial_velocity*MI_TO_M

#4
final_velocity = vConvert + acceleration*time
distance = (.5 * (final_velocity+vConvert))*time

#5a
trips = TIME/time

#5b
finalTime = TIME-(float(trips*time))



print("Congratulations! You've done it!")
print("You made", int(trips), "trips.")
print("You had", format(finalTime,'.2f'), "seconds to spare.")
print('During each trip you travelled', format(distance,'.2f'), "meters.")
print("Your final velocity was" ,format(final_velocity,'.2f'), "m/s^2.")
print('''You're free to shout, "hurray!"''') 
