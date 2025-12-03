#For loop in Python

for i in range(5): #0 to 4
    print("Iteration:", i)

for i in range(1, 6): #1 to 5
    print("Number:", i) 

for i in range(0,10,2): #0 to 9 with step 2
    print ("Even Number:", i) #0,2,4,6,8

#While loop in Python
count = 0
while count < 5: #Loop until count is less than 5
    print("Count is:", count) 
    count += 1 #Increment count by 1

#Loop Control Statements
for i in range(10):
    if i == 5:
        print("Skipping number 5")
        continue #Skip the rest of the loop when i is 5
    if i == 8:
        print("Breaking at number 8")
        break #Exit the loop when i is 8
    print("Current number:", i)

#Nested Loops
for i in range(3): #Outer loop
    for j in range(2): #Inner loop
        print(f"i: {i}, j: {j}")
#Output:
#i: 0, j: 0
#i: 0, j: 1
#i: 1, j: 0

#i: 1, j: 1
#i: 2, j: 0
#i: 2, j: 1

#Exercises:
 #1.Create a multiplication table generator.
 #2.Write a program that finds all prime numbers up to a given number.
 #(limit = 20)

#1. Multiplication Table Generator
num = 5 #You can change this number to generate a different table
print(f"Multiplication Table for {num}:")
for i in range(1, 11): #1 to 10
    print(f"{num} x {i} = {num * i}")

#2. Find all prime numbers up to a given limit
limit = 20
print(f"Prime numbers up to {limit}:")
for num in range(2, limit + 1): #Check numbers from 2 to limit
    is_prime = True
    for i in range(2, int(num**0.5) + 1): #Check divisibility
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)





