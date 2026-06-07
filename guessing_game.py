import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

while True:
    # Ask the user to guess the number
    guess = int(input("Try to guess the number: "))

    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations!")
        break
