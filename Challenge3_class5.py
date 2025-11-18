is_homeowner = False 
is_family_member= False 
is_guest= True 
homeowner_present = True 
is_emergency = False
lockdown_mode = True
current_hour = 23

identified_as = ""

person_present =  int(input ("Select 1 if homeowner, 2 if family member, 3 if guest").strip().lower())
if person_present == 1: 
    identified_as = ("homeowner") ## No need for ()

elif person_present == 2:
    identified_as = ("family member") ## No need for ()
elif person_present == 3:
    identified_as = ("guest") ## No need for ()
else: 
    print ("invalid input")


if is_emergency:
    decision = ("Access granted") ## No need for ()
elif lockdown_mode: 
   decision = ("Access denied") ## No need for ()
else: 
    if is_homeowner: 
        decision = ("Access granted") ## No need for ()
    elif is_family_member and current_hour <=23:
       decision = ("Access granted") ## No need for ()
    elif is_guest and homeowner_present and 6<=current_hour<=22:
        decision = ("Access granted") ## No need for ()
    else: 
        decision = ("Access denied") ## No need for ()
    
    
print (f"the person present is: {identified_as}")
print (f"the current time is: {current_hour}")
print (f"Is this an emergency: {'Yes' if is_emergency else 'No'} ")
print(f"Is lockdown mode on: {'Yes' if lockdown_mode else 'No'} ")
print (decision)