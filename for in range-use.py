total_sum = 0

for i in range(6):
    number = int(input("Enter a value: "))

    # Check if the number is odd, divisible by 3, and less than 500
    if number % 2 != 0 and number % 3 == 0 and 1 <= number < 500:
        total_sum += number

print(
    f"The sum of the odd numbers that are divisible by 3 and less than 500 is {total_sum}"
)
