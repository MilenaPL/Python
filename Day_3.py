print('''
*******************************************************************************
  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  ,adPPYba,
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  a8P_____88
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          8PP"""""""  
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          "8b,   ,aa 
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88           `"Ybbd8"'

*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first = input(
    'You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n')
first1 = first.lower()
if first1 == "right":
    second = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    second1 = second.lower()
    if second1 == "wait":
        third = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        third1 = third.lower()
        if third1 == "red":
            print("It's a room full of fire. Game over dude:p")
        elif third1 == "yellow":
            print("You found the treasure! You Win!")
        elif third1 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
