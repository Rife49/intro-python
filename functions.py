# A function is a block of code that only runs when its called
# we can pass data function (parameters), and they can return data as a result

#def function_name(parameters):
# code block (indented)
# prefor, actio ns using parametes 
# return value #Optional


def my_function():
    print("This is my function")
    
# calling the function
my_function()

# Functions with parameters
def print_full_name(f_name, l_name):
    print(f"this name is: {f_name} {l_name}")
    
print_full_name("Leo", "Flores")

# Functions that return values
# Instead of just printing, functions can send back (return) data

def get_full_name(f_name, l_name):
    return f"{f_name} {l_name}" # sends back the full name as text 

# store the returned value ina variable
full_name = get_full_name("Leo", "Flores")
print(full_name)

# Functions with default parameters
# A defaukt paremeters means the function will us that value 
# if no argument is provided when calling the function


def greet(name="Student"):
    print(f"Hello, {name}! Welcome to class")
    
# calking with no argument -> uses the default 
greet()

# calking with argument ->  overrides the default
greet("Leo")