import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome in Rock, Paper and Scissors game!")
human_choose = input('Write "0" to choose Rock, "1" to choose Paper and "2" to choose Scissors\n')

computer_choose = random.randint(0, 2)

human_choose = int(human_choose)

rock1 = 0
paper1 = 1
scissors1 = 2

if human_choose == scissors1:
    print("Your choice: SCISSORS")
    print(scissors)
    if computer_choose == paper1:
        print("Computer choice: PAPER")
        print(paper)
        print("Congratulations! You won!")
    elif computer_choose == rock1:
        print("Computer choice: ROCK")
        print(rock)
        print("Ohhhh no... You lost...")
    elif computer_choose == scissors1:
        print("Computer choice: SCISSORS")
        print(scissors)
        print("Nobody won")
elif human_choose == rock1:
    print("Your choice: ROCK")
    print(rock)
    if computer_choose == paper1:
        print("Computer choice: PAPER")
        print(paper)
        print("Ohhhh no... You lost...")
    elif computer_choose == rock1:
        print("Computer choice: ROCK")
        print(rock)
        print("Nobody won")
    elif computer_choose == scissors1:
        print("Computer choice: SCISSORS")
        print(scissors)
        print("Congratulations! You won!")
elif human_choose == paper1:
    print("Your choice: PAPER")
    print(paper)
    if computer_choose == paper1:
        print("Computer choice: PAPER")
        print(paper)
        print("Nobody won")
    elif computer_choose == rock1:
        print("Computer choice: ROCK")
        print(rock)
        print("Congratulations! You won!")
    elif computer_choose == scissors1:
        print("Computer choice: SCISSORS")
        print(scissors)
        print("Ohhhh no... You lost...")
else:
    print("Hmmm, check ruls again:)")
