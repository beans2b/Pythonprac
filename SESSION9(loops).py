"""CHALLENGE 1"""
#Usrint=input("put a number here: ")
#Usrint_int = int(Usrint)
#for i in range(1, Usrint_int):
#    print(i, end=" ")

"""CHALLENGE 2"""
#Usrint=input("put a letter here: ")
#Usrint_str= Usrint
#for i in range:


"""HW1"""

Balance=0

for i in range(5):
    usrRequest = input("What do you want to do(a=Withdrawl, b=deposit, c=withdraw, q=quit): ")
    usrRequest = str(usrRequest.strip(" ").lower())
    if usrRequest == "a":
        print(f"Balance is:{Balance}")

    elif usrRequest == "b":
        s = int(input("Write # amount: "))
        Balance = Balance + s
        print(f"Updated Balance:{Balance}")
        
    elif usrRequest == "c":
        d = int(input("Write # amount: "))
        Balance = Balance - d
        print (f"Updated Balance:{Balance}")

    elif usrRequest == "q":
        break
    else:
        print("INVALID INPUT, TRY AGAIN")



"""HW2"""