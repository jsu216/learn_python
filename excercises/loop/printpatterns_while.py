# ooooooooo
i = 0
while i < 9:
    print('o', end='')
    i = i + 1
print()

# 0123456789
i = 0
while i < 9:
    print(i, end='')
    i = i + 1
print()

# 0
# 2
# 4
# 6
# 8
i = 0
while i < 5:
    print(i * 2)
    i = i + 1
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

i = 0
while i < 9:
    j = 0
    while j < 9:
        print('x', end='')
        j = j + 1
    print()
    i = i + 1
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

i = 0
while i < 10:
    j = 0
    while j < i:
        print('*', end='')
        j = j + 1
    i = i + 1
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

j = 10
while j > 0:
    i = 0
    while i < j:
        print('#', end='')
        i = i + 1
    j = j - 1
    print()

print()

#     ^
#    ^^^
#   ^^^^^
#  ^^^^^^^
# ^^^^^^^^^

j = 0
while j < 9:
    i = 0
    while i < 8 - j:
        print(' ', end='')
        i = i + 1
    i = 0
    while i < (2 * j + 1):
        print('^', end='')
        i = i + 1
    j = j + 1
    print()

