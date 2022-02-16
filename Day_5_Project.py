# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Python Random choice() Method

password_letters = []

for one_letter in letters:
    if len(password_letters) < nr_letters:
        password_letters += random.choice(letters)

password_numbers = []

for one_number in numbers:
    if len(password_numbers) < nr_numbers:
        password_numbers += random.choice(numbers)

password_symbols = []

for one_symbol in symbols:
    if len(password_symbols) < nr_symbols:
        password_symbols += random.choice(symbols)

everything = password_numbers + password_letters + password_symbols

random.shuffle(everything)

listToStr = ' '.join([str(elem) for elem in everything])
# Python program to convert a list
# to string using list comprehension

print(listToStr)


###############################################################################
###################second way##################################################
###############################################################################

# Password Generator Project

#import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_l = []
for l in range(1, nr_letters + 1):
    password_l += random.choice(letters)

password_s = []
for s in range(1, nr_symbols + 1):
    password_s += random.choice(symbols)

password_n = []
for n in range(1, nr_numbers + 1):
    password_n += random.choice(numbers)

every = password_s + password_n + password_l

# random.shuffle it's working with lists, so we have to use it before convert on string
random.shuffle(every)

# for change from list to string, we using loop
password_string = ""
for ps in every:
    password_string += ps

print(password_string)
