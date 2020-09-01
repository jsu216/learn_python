my_numbers = (32, 43, 12, 4, 67)
index = 0
biggest = None
smallest = None

while index < len(my_numbers):
    if smallest is None or my_numbers[index] < smallest:
        smallest = my_numbers[index]
    if biggest is None or my_numbers[index] > biggest:
        biggest = my_numbers[index]
    index += 1

print(f"The biggest number in {my_numbers} is {biggest}")
print(f"The smallest number in {my_numbers} is {smallest}")