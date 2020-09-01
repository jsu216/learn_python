from random import randint

number = randint(1, 100)

my_guess = input("Please input a number between 1 to 100:")

print(f"Secret number is {number}. Your guess is {my_guess}")
