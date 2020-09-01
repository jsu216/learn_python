try:
    guess = int(input("Please input a number: "))
    print(f"You input a number: {guess}")
    print('blah blah')
except ValueError:
    print("You did not input a valid number.")
finally:
    print("Please try it again. This msg will always be shown.")
