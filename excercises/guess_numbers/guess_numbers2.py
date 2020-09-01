from random import randint

while True:
    guess = 0
    secret = randint(1, 100)
    print("Hey dude, I have a secret number from 1 to 100. Let's see how many times you can guess it.")
    counter = 0
    while guess != secret:
        if counter > 5:
            print("Come on dude, Focus! You guessed " + str(counter) + " times already. I bet you can do much better than that!")
        while True:
            try:
                guess = int(input())
                break
            except ValueError:
                print("Seriously, dude! Please input a valid number.")
        counter += 1
        if guess > secret:
            print("#" + str(counter) + ": Too big, try a smaller one!")
        elif guess < secret:
            print("#" + str(counter) + ": Too small, try a bigger one again!")
        else:
            print("Great! It's " + str(secret) + ". It took you " + str(counter) + " times to get it. Nice job!")
    print("Nice job! Do you want to play again (y/n)?")
    if input() != "y":
        break;
print("Let's play next time. Bye!")