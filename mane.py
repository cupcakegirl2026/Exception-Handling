try:
    number=int(input("Please enter number:"))
    print(f"You entered: {number}")
except ValueError as e:
    print(f"Invalid input.Please enter a valid number.")