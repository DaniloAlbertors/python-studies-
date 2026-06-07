number = int(input("Enter a number: "))
# This is for create a counter
counter = 1
# The use of while is for create a multiplication table
while counter <= 10:
  # The variable result stores the multiplication of the number entered by the user and the counter.
    result = number * counter
    print(f"{number} x {counter} = {result}")
    counter += 1
