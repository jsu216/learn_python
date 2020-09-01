from random import randint

secret = randint(1, 100)
print('Hey dude, I have a secret number from 1 to 100. Let\'s see how many times you can guess it.')

guess = 0
while guess != secret:
    guess = int(input())
    if guess > secret:
        print("Too big, try a smaller one!")
    elif guess < secret:
        print("Too small, try a bigger one again!")
    else:
        print("Great! It's " + str(secret))
print("Let's play next time. Bye!")