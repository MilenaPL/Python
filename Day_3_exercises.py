# even, odd number

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("It's even number!")
else:
    print("It's odd number")


# BMI calculator 2.0

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight/(height*height)
print(f"Your BMI is {round(bmi ,2)}")

if bmi <= 18.5:
    print("You are underweight")
elif bmi <= 25:
    print("You have a normal weight")
elif bmi <= 30:
    print("You are slightly overweight")
elif bmi <= 35:
    print("You are obese")
else:
    print("You are clinically obese")


# Leap year

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 != 0:
        print("This is a leap year")
    elif year % 400 == 0:
        print("This is a leap year")
    else:
        print("This isn't a leap year")
else:
    print("This isn't a leap year")


# Ordering pizza

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
    print(f"The price is ${bill}")
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
    print(f"The price is ${bill}")
else:
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
    print(f"The price is ${bill}")


# Love calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

both = name1.lower() + name2.lower()

t = int(both.count("t"))
r = int(both.count("r"))
u = int(both.count("u"))
e = int(both.count("e"))

number_of_true = t+r+u+e

l = int(both.count("l"))
o = int(both.count("o"))
v = int(both.count("v"))
e = int(both.count("e"))

number_of_love = l+o+v+e

both2 = str(number_of_true)+str(number_of_love)

both3 = int(both2)

if both3 <= 10 or both3 >= 90:
    print(f"Your score is {both3}, you go together like coke and mentos.")
elif both3 >= 40 and both3 <= 50:
    print(f"Your score is {both3}, you are alright together.")
else:
    print(f"Your score is {both3}.")
