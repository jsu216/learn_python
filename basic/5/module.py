import sys

print("How old are you?")
age = int(sys.stdin.readline())

if age < 10:
    print('You are too young to learn Python!')
elif age > 16:
    print('It''s never too late to learn Python!')
else:
    print('It''s the perfect time to learn Python!')