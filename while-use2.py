total_sum = 0
number_count = 0

while True:
    number = int(input("Enter a number: "))

    # Stop the loop if the user enters a negative number
    if number < 0:
        break

    # Add the number to the total sum
    total_sum += number

    # Count how many valid numbers were entered
    number_count += 1

# Calculate the average if at least one valid number was entered
if number_count > 0:
    average = total_sum / number_count
    print(f"The average is: {average:.2f}")
