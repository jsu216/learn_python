age = 0

while age < 100:
    print('How old are you?')
    age = int(input())

    if age < 30:
        if age <= 10:
            print('You are a baby!')
        else:
            print('You are young!')
    elif age < 60:
        print("You are in middle age!")
    else:
        print('You are old!')
print('You are %d years old. Bye bye' % age)