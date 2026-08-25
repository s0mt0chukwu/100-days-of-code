print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`           |                     |
 _________|_____________________:=._o "=._."_.-="'"=.______|___________________|_______
|     WELCOME TO    |    __.--" , ; `"=._o." ,-"""-._ ".   |                  |
|___TREASURE ISLAND_|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
''')

print("WELCOME TO TREASURE ISLAMD")
print("your mission is to find the treasure.")
choice1 = input('you\'re at a crossroad. where do you want to go?'
                ' Type "left" or "right".\n').lower()

if choice1 == "left":
    print("you've come to a lake. there ia an island in the middle of the lake.")
    choice2 = input('Type "wait" for a boat. or type "swim" to swim across.\n' ).lower()
    if choice2 == "wait":
        choice3 = input('you arrived at the island unharmed. '
              'There ia a house with 3 doors. One red, one yellow and one blue.'
              ' Which one do you choose? \n').lower()
        if choice3 == "red":
            print("it's a room full of fire. game over.")
        elif choice3 == "yellow":
            print("You found the treasure. You win!")
        elif choice3 == "blue":
            print("You entered a room of beast. Game over.")
        else:
            print('you choose a door that doesnt exist. Game over.')
else:
    print("You fell into a hole. Game .")