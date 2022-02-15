# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

# task - find average and not using len() and sum()

total = 0
for a in student_heights:
    total = total + a

number = 0
for i in student_heights:
    number += 1

avg = total/number

print(f"The average is {avg}")


# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

student_scores.sort()
print(f"Maximum value is : {student_scores[-1]}")
print(f"Minimum value is : {student_scores[0]}")

# second way

print(max(student_scores))
print(min(student_scores))

# for loop method

the_highest = 0  # it will hold the current value
for score in student_scores:
    if score > the_highest:
        the_highest = score
print(f"The highest score is : {the_highest}")


# Next task
# the sum of all the even (parzysty) numbers from 1 to 100

sum_of_even = 0
for number in range(2, 101, 2):
    sum_of_even += number

print(sum_of_even)

# different way - the sum of all the even numbers from 1 to 100

sum_of_even2 = 0
for number2 in range(1, 101):
    if number2 % 2 == 0:
        sum_of_even2 += number2
print(sum_of_even2)


# write Fizz Buzz game

for num in range(1, 101):
    if num % 3 == 0 and num % 5 != 0:
        print("Fizz")
    if num % 5 == 0 and num % 3 != 0:
        print("Buzz")
    if num % 3 == 0 and num % 5 == 0:
        print("Fizz Buzz")
    if num % 3 != 0 and num % 5 != 0:
        print(num)
