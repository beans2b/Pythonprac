
#is_homeowner = True
#is_familymember= False
#Is_guest = True
#homeowner_present = False
#is_emergency= False
#lockdown_mode= True
#current_hour= 23

#if is_emergency:
    #print("allow total access")

#elif lockdown_mode:
    #print("no one can enter")

#else:
    #print("Please verify your identity")

    #if is_homeowner:
        #print("Allow access")

    #elif is_familymember and current_hour < 23:
        #print("Allow access")

    #elif Is_guest and homeowner_present and current_hour > 6 and current_hour < 22:
        #print("Allow acesss")

    #else:
        #print("deny entry")

"""2"""

#c_user = "admin"
#c_pass ="banana"

#userpass= input("write password")
#useruser= input("write user")

#userpass = userpass.lower()
#useruser = useruser.lower()

#if userpass == c_pass and useruser == c_user:
   # print("Access granted")

#else:
    #print("incorrect password, try again")
    

"""3"""
#number = 0

#if number > 0:
    #print("number is positive")
#elif number < 0:
    #print("number is negative")

#else: 
   # print("number is 0")


"""4"""

gpa = float(input("write gpa number: "))
Service = int(input("Did community service yes=1, no=2"))

if gpa > 3.5:
    if Service == 1:
        print("quialifies for full scolarship")
    else: 
        print("partial scolarship")

elif gpa > 3.0:
    Sports= int(input("did sports yes=1, no=2"))

    if Sports == 1:
        print("quilifies for sports scolarship")
    else:
        print("doesnt quialify for scolarhip")

else:
   print("no scolarship")
