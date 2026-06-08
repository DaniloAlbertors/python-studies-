def factorial(number=1):
    result = 1
    for i in range(number, 0, -1):
        result *= i
    return result
# enter the number for factorial calculation
user_number = int(input("Enter a number: "))

# Verification for negative numbers
if user_number < 0:
    print("The factorial of a negative number does not exist in mathematics.")
else:
    print(f"The factorial of {user_number} is {factorial(user_number)}")
