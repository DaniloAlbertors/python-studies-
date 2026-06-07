years = int(input("How old are you (in years)? "))
months = int(input("How many months after your last birthday? "))
days = int(input("How many days after the completed months? "))

## User age calculation
age_in_days = (years * 365) + (months * 30) + days

print("Your age in days is", age_in_days)
