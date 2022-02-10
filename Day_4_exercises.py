#
# Coin toss
#
import random

random_integer = random.randint(1, 2)

if random_integer == 1:
    print('Heads')
else:
    print('Tails')




#
# Who will pay the bill ?
#

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# don't forget import random

how_many = len(names)  # here is counting from 1   - number of items
x = how_many - 1      # but we need to count from 0
people_in_restaurant = random.randint(0, x)

print(
    f"Today, the winner is {names[people_in_restaurant]}! You have to pay all bill:p")


# easier way to solve who is gonna pay

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# don't forget import random
print(f"Today {random.choice(names)} pay!")




#
#  create treasure map
#

row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# columns are counted first 1, 2, 3, after this we add row 1, 2, 3

if position == "11":
  row1[0] = "X"
elif position == "12":
  row2[0] = "X"
elif position == "13":
  row3[0] = "X"
elif position == "21":
  row1[1] = "X"
elif position == "22":
  row2[1] = "X"
elif position == "23":
  row3[1] = "X"
elif position == "31":
  row1[2] = "X"
elif position == "32":
  row2[2] = "X"
elif position == "33":
  row3[2] = "X"

print(f"{row1}\n{row2}\n{row3}"){row3}")



# create treasure map - easier way
# Angela's idea

row1=["⬜️", "⬜️", "⬜️"]
row2=["⬜️", "⬜️", "⬜️"]
row3=["⬜️", "⬜️", "⬜️"]
map=[row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("Where do you want to put the treasure? ")

vertical=int(position[1])
horizontal=int(position[0])

selected_row=map[vertical-1]
selected_row[horizontal-1]="X"

print(f"{row1}\n{row2}\n{row3}"){row3}")
