age = input("enter Age: ").strip()
if age.isdigit():
    age = int(age)
    print(f"Your age is {age}")
else:
    print("Invalid age entered")

child= 5.00
teen= 8.00
adult= 12.00
senior= 7.00
dis_flo= 2.00

student = input("enter status yes/no: ")
if student not in["no","yes"]:
    print ("Invalid student status")

if age > 0 and age < 12 and student == "yes":
    print(f"price is ${child - dis_flo}")
elif student == "no":
    print(f"price is ${child}")

elif age > 13 and age < 17 and student == "yes":
    print(f"price is $= {teen - dis_flo}")
elif student == "no":
    print(f"price is ${teen}")

elif age > 18 and age < 64 and student == "yes":
    print(f"price is = ${adult - dis_flo}")
elif student == "no":
    print(f"price is ${adult}")

elif age > 65 and student == "yes":
 print(f"price is = ${senior - dis_flo}")
elif student == "no":
    print(f"price is ${senior}")
