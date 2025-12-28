import random

"""" Mini TASK 1

names =["jobber","gobber","pooper","dumber","stoner"]

for i in range(3): 
    print(random.choice(names))

old_names=names.copy()
random.shuffle(names)

print("old order: ",old_names)
print("new order: ",names)"""

"""Mini task 2: 1. random — Simple Game Logic

import random
print(random.randint(1,10))
lotto = random.randint(1,10)

for r in range(3):
    guess = int(input("Pick a number under 10"))

    if  guess == lotto:
        print("You guessed correct")
        break
    elif guess > lotto:
        print("too high")
    elif guess <lotto:
        print("too low")
else:
    print(f"Sorry, the correct number was {lotto}")"""

