#Welcome to BMI calculator! This app takes your height and weight and computes your Body Mass Index and tells you it's clinical significance.

# Get the height and weight
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#W BMI=weight/height squared
bmi = float(weight)/float(height)**2
print(int(bmi))

if bmi <=18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi <=25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi <=30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi <=35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")