listeven = 0
listodd = 0
sumeven= 0
sumodd = 0 

for i in range (1,11):
    num = int(input(f"Insert number{i}:"))
    if i % 2 == 0:
        listeven += 1
        sumeven +=i
        
    else:
        listodd += 1 
        sumodd +=i

print("Results:")
print("Even numbers:",listeven)
print("Odd numbers:",listodd)
print("Sum of even numbers", sumeven)
print("Sum of odd numbers:", sumodd)
