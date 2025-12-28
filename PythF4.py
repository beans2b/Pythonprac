import random

rolls = []
dicer = int(input("how many dice rolls? "))

for i in range(dicer):
    print ("Rolling dice...")
    generate = random.randint(1,6)
    rolls.append(generate)
high = max(rolls)
low = min(rolls)
avg = sum(rolls)/len(rolls)
tot= sum(rolls)

print("Rolls:", rolls)
print("Highest roll:", high)
print("Lowest roll:", low)
print(f"Average:{avg:.2f}")
print("Total sum:", tot)
    