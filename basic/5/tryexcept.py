try:
    guess = int(input("Please input a number"))
    print(f"You input a number: {guess}")
except ValueError:
    print("Please input a valid number.")