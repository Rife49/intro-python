# Arithmetic operators - mathematical operation
# if you have typed it enoough use Tab to auto fill the rest in terminal
x = 1
y = 2
res = 0 

res = x // y # +, -, *, /, %, **, //
print(res)

# assignment operators - used to assign values to variables 
# += all opoerators have to be before = 
x = 5
x += 5 
x -= 3
x *= 3
x /= 3
print(x)

# comparison operators
# used to compare 2 values - same as the if else statement 

# == (equal to), !=(not equal), <> (less/greater than), <= >=

# logical operators - used to combine cionditional statements
# used with True/False value like conditions
# and -> both must be True 
# or -> at least one must be True

x = 10
y = 10 
z = 3

print(x == y and y == z) # False, because both conditions are Not true 
print( x ==y or y == z ) # True, because at least one condition is true
print(not x == y ) # False, because x ==y are the same

# Identity operators - used to compare the objects, not if there equal
# but if they are actually the same object with the same memory location
# is -> checks if 2 things are the extact same object in memory 
# is not -> checks if the are NOT the same 

x = 3 
y = 3 
print(x is y ) #. Returns true since they are the same 
print( x is not y) # returnd false since they are the same 

# Membership operators - used to test if a sequence is presented in an object
# in -> checks if something exist inside the sequence (list, strings etc...)
# not in -> check if something is not inside 

x = [1, 2, 3, 4, 5] # this is a list 

print(4 in x ) # True 4 is in
print( 9 not in x ) #True because 9 isn't