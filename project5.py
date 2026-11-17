
import random

print("================================")
print("        RANDOM FUN CALCULATOR")
print("================================")

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

print("First random number:", num1)
print("Second random number:", num2)

print("\n========== CALCULATIONS ==========")

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", round(num1 / num2, 2))

print("Square of first number:", num1 ** 2)
print("Cube of second number:", num2 ** 3)

print("\n========== COMPARISON ==========")

if num1 > num2:
    print("The first number is greater.")
elif num2 > num1:
    print("The second number is greater.")
else:
    print("Both numbers are equal.")

print("\n========== LUCKY NUMBER ==========")

lucky = random.randint(1, 100)

print("Your lucky number is:", lucky)

if lucky >= 50:
    print("You got a high lucky number!")
else:
    print("You got a low lucky number!")

print("\nThanks for playing!")
