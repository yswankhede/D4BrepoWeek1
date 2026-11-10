user_input = input("Enter a number: ")
try:
    number = float(user_input)
    print(f"You entered: {number}")
    print("Type:", type(number))
except ValueError:
    print("Invalid input! Please enter a numeric value.")
    