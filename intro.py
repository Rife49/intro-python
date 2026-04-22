print("Hell World from Python!")
print(2)
print(5 + 3)
print(True)


# This is a comment 
# ctl + s Save File 
# Up arrow key in terminal to see previous commands 

"""

Everything  inside is a comment
Useful guide/ code breakdown 
"""

# Create a varriable
name = "Rife"
age = 17
print(name)

print("My name is: " + name + ", and I am " + str(age)  + "years old.")

name = "Rife"
age = 18
middle_name = "Jesse"
last_name = "Ariana"
found = False

print("My name is: " + name + " " + middle_name + " " + last_name + " my age is: " + str(age)  + "years old.")

# f-string
print(f"My name is: {name} {middle_name} {last_name} my age is: {age}")
# to cll variables wrap in{}
# no need for converting with str()

name = "Burnt"
age = 2
middle_name = "Buttery"
last_name = "Toast"
found = True 

print("I: " + name + " " + middle_name + " " + last_name + " pieces: " + str(age)  + ".")

print(f"I: {name} {middle_name} {last_name} pieces: {age}")

#type functions 
print(type(name))
print(type(age))
print(type(True))

# Casting (Changing data types)
print(20+ int("20"))
print(20+ age)
print(20+ 2.98)

# Input Function
user_name = input("Enter your name: ")
print(f"Hello, {user_name}")

# input() alwyas returns a string 
print(type(input("Enter your age: ")))

new_age = int(input("Enter your age: "))
print(age + new_age)

