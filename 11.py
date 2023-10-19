try:
    x = float(input("Enter a number (X): "))
    y = int(input("Enter the power (Y): "))

    result = x ** y
    print(f"{x} to the power of {y} is {result}")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
