""""INPUTS"""
##input() is a built-in Python function that pauses your program and waits for the user to type something.

#first_name = input("Whats ur firs name?: ")
#last_name = input("whats your last name?: ")

#print(f"Hello, {first_name},{last_name}")
""""INPUTS + STRING TO FLOAT CONVERSION"""

#Celsius = input("Celsius degrees")
#Celsius_flo = float(Celsius)
#Fahrenheit= (Celsius_flo*9/5) + 32

#print(f"Fahrenheit is, {Fahrenheit:.1f}")

"""BASIC IMPUT"""

#enter_product_name= input("Enter product code:  ")
#enter_product_name_stri = enter_product_name.upper().strip()

#print(f"Product: {enter_product_name}")
#print(f"Product: {enter_product_name_stri}")


"""Simple Profile Generator"""
#• Profile Builder:
#Ask the user for their: First Name, Last Name, Age, Favorite Programming Language
#• Use .strip() on both names to remove accidental leading/trailing spaces.
#• Convert the Age input to an integer.
#• Print a summary profile using f-strings, clearly labeling each piece of information.
#• Include a decorative separator line (e.g., --- User Profile ---) using string repetition.
#Example Output:
#--- User Profile ---
#Name: Jane Smith
#Age: 30 years old
#Favorite Language: Python

#first_name = input("whats ur first name?")
#last_name = input("whats ur last name?")
#age = input("whats ur age?")
#age_int= int(age)
#fav_prog_lag = input(" whats ur favorite programming language?")
separator = "-"*20

#print(separator,"USER PROFILE",separator)
#print(f"First name:{first_name}") 
#print(f"last name:{last_name}") 
#print(f"age:{age_int}years old.")
#print(f"favorite proggraming language: {fav_prog_lag}")
#print(separator)

"""Basic Tip Calculator"""
#• Tip Calculation:
#• Ask the user for the total_bill_amount (as a number).
#• Ask the user for the desired_tip_percentage (e.g., 15 for 15%, 20 for 20%).
#• Crucial: Convert both inputs to appropriate numerical types (float or int).
#• Calculate the tip_amount.
#• Calculate the total_bill_with_tip.
#• Print the total_bill_with_tip using an f-string, formatted to two decimal places and including a
#currency symbol (e.g., €).
#• Example Output:
#Enter total bill amount: 50
#Enter desired tip percentage (e.g., 15 for 15%): 20
#Total with tip: €60.00

#total_bill_amount = input("total bill amount:")
#desired_percentage = input("desired percentage:")
#bills_conv = int(total_bill_amount)
#percentage_conv = int(desired_percentage)
#tip_amount = bills_conv%percentage_conv
#total_bill_tip = tip_amount + bills_conv

#print(f"tip amount {tip_amount}")
#print(f"total amount: ${total_bill_tip:.2f}")

"""Exercise1"""

#Print out this welcome message on
#python!
#Example output:
#+-----------------+
#| WELCOME |
#+-----------------+

Pl_us = "+"
Si_gn = "|"
 
print(Pl_us,separator,Pl_us)
print(Si_gn,"WELCOME",Si_gn, sep="       ")
print(Pl_us,separator,Pl_us)

"""Exercise1 Correction"""

# Box with centered text
text = "WELCOME"
border = "+" + "-" * (len(text) + 4) + "+"
middle = "| " + text + " |"
print(border)
print(middle)
print(border)
