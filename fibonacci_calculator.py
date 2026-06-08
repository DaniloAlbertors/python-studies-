def fibonacci(n):
    # Handle base cases: the 0th and 1st positions of the sequence
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    previous = 0
    current = 1
    
    # Iteratively calculate the next numbers by summing the previous two
    for i in range(2, n + 1):
        next_num = previous + current
        previous = current
        current = next_num
        
    return current


user_number = int(input("Enter the position in the Fibonacci sequence you want to find: "))
print(f"The value at position {user_number} is: {fibonacci(user_number)}")

continue_choice = input("Do you want to continue? [Y/N]: ")

while continue_choice.upper() != "N":
    user_number = int(input("Enter the position in the Fibonacci sequence you want to find: "))
    print(f"The value at position {user_number} is: {fibonacci(user_number)}")
    continue_choice = input("Do you want to continue? [Y/N]: ")

print("Program ended!")
