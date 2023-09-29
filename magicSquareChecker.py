import numpy as np
from itertools import permutations
import math

def is_magic_square(square):
    # Calculate the sum of the first row
    magic_sum = sum(square[0])

    # Check rows and columns
    for i in range(len(square)):
        if sum(square[i]) != magic_sum or sum(square[:, i]) != magic_sum:
            return False

    # Check diagonals
    if square.trace() != magic_sum or np.fliplr(square).trace() != magic_sum:
        return False

    return True

def check_any_square(numbers):
    # Check if the number of inputs is a perfect square
    root = math.isqrt(len(numbers))
    if root ** 2 != len(numbers):
        print("The number of inputs is not a perfect square. No squares to check.")
        return

    for perm in permutations(numbers):
        square = np.array(perm).reshape((root, root))
        if is_magic_square(square):
            print(f"A magic square exists among the permutations of the input numbers. One such magic square is:\n{square}")
            return
    print("No magic square exists among the permutations of the input numbers.")

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
check_any_square(numbers)
