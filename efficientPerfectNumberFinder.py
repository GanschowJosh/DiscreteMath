def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def perfect_numbers(n):
    for p in range(2, n):
        m = (1 << p) - 1
        if is_prime(m):
            perfect_num = (1 << (p - 1)) * m
            if perfect_num <= n:
                print(perfect_num)

# Call the function with the range you want to check for perfect numbers
perfect_numbers(int(input("Find perfect numbers up to: ")))
