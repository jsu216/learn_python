# for element in range(1, 5):
#     print(element)
#
# wizard_list = ['spider legs', 'toe of frog', 'snail tongue', 'bat wing', 'slug butter', 'bear burp']
# for i in wizard_list:
#     print(i)
#
my_numbers = (3, 5, 12, 34, 8, 9)
#
# for number in my_numbers:
#     if number < 10:
#         print(number)

smallest = 100
biggest = 0
for number in my_numbers:
    if number < smallest:
        smallest = number
    elif number > biggest:
        biggest = number

print(f"Smallest number in {my_numbers} is {smallest}")
print(f"Biggest number in {my_numbers} is {biggest}")
