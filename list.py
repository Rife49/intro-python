# list are written with square brackets []

my_list = [10, 20, 30, 40, 50]
print(my_list)

# List can contain diffrent data types
mixed_list = [1, "apple", 3.5, True]
print(mixed_list)

# Access by their index number 
# (Indexing alwasy starts at 0)

fruits = ["apple", "banana", "cherry"]
print(fruits[0]) 
print(fruits[1]) 
print(fruits[2]) 

# you can also negtive indexes to count from the end
print(fruits[-1])

# Modifying list items
fruits[1] = "mango"
print(fruits)

# Add items to a list 
fruits.append("orange")
print(fruits)

fruits.insert(1,"kiwi")
print(fruits)

# Removing items
fruits.remove("cherry")
print(fruits)

# Removes the last item 
fruits.pop() 
print(fruits)

# Looping through a list
for fruit in fruits:
    print(fruit)

# check if item exist
if "mango" in fruits:
    print("yes, mango is in the list")

# List length
print(len(fruits))

movies = ["Moana", "12 strong", "step brothers", "shrek"]
print(movies[0])
print(movies[1])
print(movies[2])
print(movies[3])






# Homework
movies = ["Moana", "12 strong", "step brothers", "shrek"]
print(movies[0])
print(movies[1])
print(movies[2])
print(movies[3])

movies[3] = "Moana 2"
print(movies)

movies.remove("Moana 2")
print(movies)






