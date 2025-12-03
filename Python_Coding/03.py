# Input and Output Validation

name = input("Enter your name: ")
height = float(input("Enter your height in cm: "))  #Convert to float

#Input validation
while True:
    try:
        age = int(input("Enter your age: "))  #Convert to integer
        if age > 0:
            break   #Valid age
        else:
            print("Please enter a positive integer for age.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for age.")

#Output Validation
print(f"Hello, {name}!")
print(f"you are {age} years old and {height} cm tall.") 

 #Exercises:
 #1.Create a simple calculator that takes two number and an operation from user.
 #2.Create a simple quiz program with 3 questions. 
 # At the end of the quiz,display score.

# Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operation"
print(f"Result: {result}")
