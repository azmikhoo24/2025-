#if-else: 2 conditions
age = 10
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# if-elif-else: multiple conditions
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Your grade is: {grade}")

#and: both conditions must be true
user_age = 25
has_license = True

if user_age >= 18 and has_license:
    print("You can drive.")
else:
    print("You cannot drive.")

#or: at least one condition must be true
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday.")

#Nested conditions: Conditions within conditions
weather = "sunny"
temperature = 75

if weather == "sunny":
    if temperature > 70:
        print("It's a nice day for a walk.")
    else:
        print("It's sunny but a bit chilly.")

#Exercise:
#Write a program that categorizes BMI (Body Mass Index) into
#underweight(<18.5), normal weight(<24.9), overweight(<29.9), and
#obesity(<30.0). (formula = kg/m^2)
weight_kg = input ("Enter your weight in kg: ")
height_m = input ("Enter your height in meters: ")

bmi = float(weight_kg) / (float(height_m) ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 24.9:
    category = "Normal weight"
elif bmi < 29.9:
    category = "Overweight"
else:
    category = "Obesity"
print(f"Your BMI is {bmi:.2f}, categorized as {category}.")
