import random

a = random.randint(1,7)

count = 0

while count < 6:
    b = random.randint(1,7)
    if a == b:
        print("You dead")
        break
    elif a!=b:
        print("You live")
        count += 1

if count == 6:
    print("You win")