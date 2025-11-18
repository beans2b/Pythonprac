body_height = float(input("enter height in cm: ").strip())
body_weight = float(input("enter weight in kg: ").strip())

body_height_m= (body_height/100)**2

bmi = body_weight/body_height_m

match bmi: 
     case _ if bmi <= 16: 
      print("severly underweight")
     
     case _ if bmi > 16 and bmi <= 18.5:
        print("underweight")
     
     case _ if bmi > 18.5 and bmi <= 25:
        print("healthy")
     
     case _ if bmi > 25 and bmi <=30:
        print("overweight")

print(f"Bmi:{bmi:.1f}")

if bmi > 30: print("severly overweight")
