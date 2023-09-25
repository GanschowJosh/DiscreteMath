"""
find contradiction to "if x|(a+b) then x|a or x|b"
"""
from random import randint

def find_contradiction(x):
    while True:
        a = randint(1, x - 1)  # Generate a random value for a between 1 and (x - 1)
        b = randint(1, x - 1)  # Generate a random value for b between 1 and (x - 1)

        if (a + b) % x == 0 and (a % x != 0 or b % x != 0):
            # Found a contradiction
            return a, b

# Get user input for x
x = int(input("Enter the value of x: "))

# Find a contradiction
a, b = find_contradiction(x)

print(f"For x = {x}, a = {a}, b = {b} contradicts the statement.")
print(f"{x}|({a} + {b}) is {(a + b) % x == 0}")
print(f"{x}|{a} is {a % x == 0}")
print(f"{x}|{b} is {b % x == 0}")
