height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
a = float(height) * float(height)
b = int(weight)
bmi = int(b/a)
print(bmi)
if bmi < 18.5:
 print("underweight")

elif bmi > 18.5 and bmi < 25:
 print("normal weight")

elif bmi > 25 and bmi < 30: 
 print("slightly overweight")

elif bmi > 30 and bmi < 35:
 print("obese")

elif bmi > 35:
 print("clinically obese")




#Under 18.5 they are underweight
#Over 18.5 but below 25 they have a normal weight
#Over 25 but below 30 they are slightly overweight
#Over 30 but below 35 they are obese
#Above 35 they are clinically obese.