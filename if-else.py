"""

if condition:
    - Code block hthat runs if the condition is true
elif (else-if)
    - code blocks runs if the firdt condition is false
    - and this condition only worls if its true 
else: 
    - Code block runs if none of the above conditions are true
"""

x = 5

if  x > 0:
    print("x is postive")
elif x == 0:
    print("x is zero")
elif x >= 5:
    print("x equals 5")
else: 
    print("x is not a positive number")

# Short hand if statements
if x > 5: print("x is greater than 5")

x = 21
# Short hand if elif statements
print("Even") if x % 2 == 0 else print("odd")

x = 25
# Nested if statements
if x > 0 :
    if x < 20:
        print(" x is a posisitve number less than 20 ")

# Combining conditions 
age = 18 

if age >= 18 and  age <= 21:
    print("You are between 18 and 21")

Temperature = int(input("Enter todays temperature in fahrenheit"))

if  Temperature >= 86:
    print("its hot outside!")
elif  Temperature >= 68 and Temperature <= 86:
    print("The weather is nice!")
elif  Temperature >= 50 and Temperature <= 68:
    print("its a bit chilly!")

