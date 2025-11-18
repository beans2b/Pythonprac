# Ask for GPA
gpa = float(input("Enter your GPA: "))

# Initialize scholarship result
scholarship = "No Scholarship"

# Apply rules
if gpa >= 3.5:
    community_service = input("Do you do community service? (yes/no): ").strip().lower()
    if community_service == "yes":
        scholarship = "Full Scholarship"
    else:
        scholarship = "Partial Scholarship"
elif 3.0 <= gpa < 3.5:
    sports = input("Do you do sports? (yes/no): ").strip().lower()
    if sports == "yes":
        scholarship = "Sports Scholarship"
    else:
        scholarship = "No Scholarship"
else:
    scholarship = "No Scholarship"

# Display result
print(f"Result: {scholarship}")