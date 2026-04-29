# a for loop is a control structure that let you repeate a block of code for each sequence
# for vriable in sequence: #code block runs for each item in sequence

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
    
print("______________________________________")
    
for letter in "Rife":
    print(letter)
    
print("______________________________________")

# Range() generates a seequnce of numbers 
for x in range(5):
    print(x)
    
print("______________________________________")

# Start and end range
for x in range(2, 6):
    print(x)
    
print("______________________________________")

# Using step
for x in range(0, 10, 2): # step just skips
    print(x)
    



#num = int(input("enter a number: "))
#for i in range (1, 11):
    #rint(f"{num} x {i} = {num * i}")
    
    
# While loops: a while look repeats a block of code as long as a condition is true 
# Be creful if the condition never become false you will get an infinite loop
# Whille condition: # Code block runs as long as condition is true 



count = 1 

while count <= 5 :
    print ("Count is: ", count)
    count += 1
    
    # Using break to stop the loop 
    
    number = 0 
    
    while True:      # Ifinite loop
        print(number)
        number += 1 
        if number == 3:
            break
        
print("______________________________________")

# Using continue tp skip an iteration
count = 0 
while count < 5:
    count += 1 
    if count == 3:
        continue
    print(count)
    
print("______________________________________")

# else with while
count = 1 
while count < 3:
    print(count)
    count += 1 
else:print("loop is finished")




password = ""
while password != "Secret123":       # start with empty string
    password = input("enter Password: ") # keep looping while password is wrong 
    if password != "Secret123":     # If wrong 
        print("Wrong! Try Again!")
# Once they type "Secret123", the while condition becomes false, so the loop stops
# print("Access Granted!")   
print("Access Granted")



