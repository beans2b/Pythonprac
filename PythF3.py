def cel_fa(celsius):
    fa = (celsius*9/5)+32
    return fa

def fa(faren):
    cel = (faren-32)*5/9
    return cel

choice = int(input("type 1 if Cel to Fah, type 2 if Fah to Cel: "))
temp = float(input("enter temperature: "))

if choice == 1:
    Celcius = cel_fa(temp)
    print(f"{temp}C {Celcius:.2f} F")
elif choice == 2: 
    Farenheit = fa(temp)
    print(f"{temp}F {Farenheit:.2f} C ")
else: 
    print("invalid choice")
    