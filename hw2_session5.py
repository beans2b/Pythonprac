# Ask for user's age
age = int(input("Enter your age: "))

# Initialize base price
price = 10

# Apply pricing rules
if age < 12:
    price = 5
elif age >= 65:
    price = 7
else:
    # For ages between 12 and 64
    student = input("Are you a student? (yes/no): ").strip().lower()
    if student == "yes":
        price = 8
    else:
        price = 10

# Display result
print(f"The ticket price is ${price}.")