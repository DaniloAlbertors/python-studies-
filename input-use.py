name = input("What is your name? ")
birth_year = int(input("What year were you born? "))
current_year = int(input("What year are we in? "))
# User age calculation
age = current_year - birth_year

print(f"Your name is {name} and you are {age} years old")
