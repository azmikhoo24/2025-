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