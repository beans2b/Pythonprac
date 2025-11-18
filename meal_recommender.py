
vegetarian = True
spicy = True

what_u = input("are you vegetarian?(yes/no): ")
spicy_u = what_u = input("Do you like spicy food? (yes/no): ")

if what_u == "yes":
    vegetarian = True
elif what_u == "no":
    vegetarian = False
else:
    print("Invalid imput")

if spicy_u == "yes":
    spicy = True
elif spicy_u == "no":
    spicy = False
else:
    print("Invalid imput")


if vegetarian == True and spicy == True:
    print("Try Spicy Lentil Curry!")
elif vegetarian == True and spicy == False:
    print("How about a Vegetable Lasagna?")
elif vegetarian == False and spicy == True:
    print("Spicy Chicken Stir-fry is for you!")
elif vegetarian == False and spicy == False:
    print ("Classic Roast Beef might be good!")

else:
    print("Nothing matches your criteria")