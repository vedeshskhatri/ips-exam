#3.Check whether a number is a Armstrong number 


num = int(input("Enter a number: "))

# Convert number to string to easily get digits
digits = str(num)
power = len(digits)

# Calculate sum of digits raised to the power
sum_of_powers = sum(int(d)**power for d in digits)

# Check if Armstrong
if sum_of_powers == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")