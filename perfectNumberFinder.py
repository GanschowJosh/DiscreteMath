def perfect_numbers(n):
    for num in range(1, n+1):
        sum = 0
        for i in range(1, num):
            if(num % i == 0):
                sum = sum + i
        if (sum == num):
            print(num)

# Call the function with the range you want to check for perfect numbers
perfect_numbers(int(input("Find perfect numbers up to: ")))
