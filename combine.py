age = 9
if age:
    print(age)
else:
    print("No age? %s" % age)

name = "Baba"
age = 45
if age < 11 and name == "Jeremy":
    print('You are %s. You are only %d years old.' % (name, age))
elif age >= 10 and name == "Jason":
    print("Hey %s, you are %d years old" % (name, age))
elif age > 9 and name == "Jason" or age < 12:
    print(f"{name}_:_{age}")
else:
    print("Come on! I don't get it: %s:%d" % (name, age))