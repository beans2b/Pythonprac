"""THIS IS FOR SETS"""
#color = {"black","white","yellow","brown","red"}
#color.add("blue") 
#color.remove("black")

#print("blue"in color)
#print (color)
"""Set Operations (Mathematical)"""
#a = {10, 20, 30, 40}
#b = {30, 40, 50, 60}

#print(a|b)
#print(a-b)
#print(b-a)
#print(a^b)

"""In-Class Assignments #4 (conditionals)"""

#color={"red","green","blue"}
#usr_inp= input("Enter a color:")

#print(f"YESSS it is:{usr_inp in color}")

"""In-class Challenge #5//HW2"""

with open("Data on customers.txt","w") as file1:
    file1.write("""alex
mary
john
sara
linda
peter
emily
james
karen
victor""")

with open("Data on purchases.txt","w") as file2:
   file2.write("""john
sara
linda
paul
emily
helen
mike
victor""")

with open("Data on customers.txt", "r")as f1:
   custo = f1.readlines()

with open("Data on purchases.txt", "r")as f2: 
   purcha = f2.readlines()

namecusto = set(custo.strip("\n"))
namepurcha = set(purcha.strip("\n"))

print(f"resgisterd customers but never purchased:{namecusto-namepurcha}")

"""HW1"""

#with open("hw1.txt","w")as hw1:
#    hw1.write("This is a hw1 text , pleaseeeee\n can you helppppp me pleaseee\n this no no no i cant")

#with open ("hw1.txt","r") as hw11:
#    home= hw11.read()
#home = home.replace(","," ").lower()

#wordcount = home.split()

#wordcountrepeat= set(wordcount)

#print(f"total unique words:{len(wordcountrepeat)}")


"""HW2"""





