my_numbers = (3, 5, 12, 34, 99999999, 9)

smallest = None
biggest = None

for number in my_numbers:
    if smallest is None or number < smallest:
        smallest = number
    if biggest is None or number > biggest:
        biggest = number

print(f"Biggest number is {biggest}")
print(f"Smallest number is {smallest}")