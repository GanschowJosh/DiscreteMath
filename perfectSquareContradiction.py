"""
Finding counterexample for If a and b are not perfect squares and a !=  b, then ab is not a perfect square
"""
import math

def find_a_and_b():
    for a in range(1, 100):
        for b in range(a + 1, 100):
            if math.isqrt(a) ** 2 != a and math.isqrt(b) ** 2 != b and math.isqrt(a * b) ** 2 == a * b:
                return a, b

a, b = find_a_and_b()
print(f"a = {a}, b = {b}")
