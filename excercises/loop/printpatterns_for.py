# ooooooooo
for i in range(9):
    print('o', end='')
print()

# 0123456789
for i in range(9):
    print(i, end='')
print()

# 0
# 2
# 4
# 6
# 8
for i in range(5):
    print(i * 2)
print()

# 1
# 3
# 5
# 7
# 9
for i in range(1, 10, 2):
    print(i)
print()

# xxxxxxxxx
# xxxxxxxxx
# xxxxxxxxx
# xxxxxxxxx
# xxxxxxxxx
# xxxxxxxxx
# xxxxxxxxx
# xxxxxxxxx
# xxxxxxxxx
# xxxxxxxxx

for i in range(9):
    for j in range(9):
        print('x', end='')
    print()
print()

# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********

for i in range(10):
    for j in range(i):
        print(i, end='')
    print()
print()

#########
########
#######
######
#####
####
###
##
#

for j in range(10, 0, -1):
    for i in range(j):
        print('#', end='')
    print()

print()

#     ^
#    ^^^
#   ^^^^^
#  ^^^^^^^
# ^^^^^^^^^

for j in range(9):
    for i in range(9 - j):
        print(' ', end='')
    for i in range(2 * j - 1):
        print('^', end='')
    print()
