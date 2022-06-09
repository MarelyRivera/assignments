# Problem 1
capitals = ['Springfield', 'Madison', 'Indianapolis', 'Denver', 'Atlanta']
states = ['Illinois', 'Wisconsin', 'Indiana', 'Colorado', 'Georgia']
dictionary = {}
dictionary = {capitals[0]:states[0], capitals[1]:states[1], capitals[2]:states[2], capitals[3]:states[3],
              capitals[4]:states[4]}

print(dictionary)


# Problem 2
question = input('Would you like to add any capitals (and their corresponding states)'
                       'to the dictionary? (y/n) ')
if question == 'y':
    new_capital = input('Enter a new capital: ')
    new_state = input('Enter the corresponding state: ')
    dictionary[new_capital] = [new_state]
    for value in dictionary:
        print(value)
