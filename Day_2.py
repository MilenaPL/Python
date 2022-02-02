# addiction number in string

two_digit_number = input("Type a two digit number: ")

first = two_digit_number[0]
second = two_digit_number[1]

print(int(first)+int(second))


# BMI calculator

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height_num = float(height)
weight_num = float(weight)

print("Your BMI is:")
print(weight_num/height_num**2)


# Life in days if you will live 90 years

age = input("What is your current age?")

years = (90 - int(age))

days = (years * 365)
weeks = (years * 52)
months = (years * 12)

print(f"You have {days} days, or {weeks} weeks, or {months} months left.")


# Tip calculator - 2 decimal places

print("Welcome to tip calculator!")
bill = input("What was the total bill?")
bill = input("What was the total bill? $")
amount_of_tip = input(
    "How much tip would you like to give? 10, 12 or 15% ? - enter a number")
    "How much tip would you like to give? 10, 12 or 15% ? -enter a number")
how_many_people = input("How many people to split the bill?")

total_bill = float(bill)
total_bill = int(bill)
percent_num = int(amount_of_tip)
tip = (percent_num/100) * total_bill
people = int(how_many_people)
each_person = (total_bill + tip) / people
each_person2 = round(each_person, 2)

print(f"Each person should pay $ {each_person2}")
