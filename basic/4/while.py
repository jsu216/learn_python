print("While loop #1")

step = 0
while step < 10:
    print(step)
    step = step + 1

print("While loop #2")

step = 0
while True:
    print(step)
    step += 1
    if step > 9:
        break