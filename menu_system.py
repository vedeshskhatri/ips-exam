def factorial(n):
    """Return factorial of n (n!)."""
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def single_digit_sum(n):
    """Condense a number into a single digit by repeated digit sum."""
    n = abs(n)          
    while n > 9:        
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        n = s
    return n

def is_armstrong(n):
    """Check whether a number is an Armstrong number."""
    num_str = str(n)
    power = len(num_str)
    total = 0
    for ch in num_str:
        total += int(ch) ** power
    return total == n

while True:
    print("\nMini Calculator Menu")
    print("1. Calculate factorial")
    print("2. Condense number to single digit (repeated digit sum)")
    print("3. Check Armstrong number")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print("Factorial of", num, "=", factorial(num))

    elif choice == 2:
        num = int(input("Enter an integer: "))
        print("Single digit sum of", num, "=", single_digit_sum(num))

    elif choice == 3:
        num = int(input("Enter a number: "))
        if is_armstrong(num):
            print(num, "is an Armstrong number.")
        else:
            print(num, "is NOT an Armstrong number.")

    elif choice == 4:
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1–4.")