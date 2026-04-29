# unordered, unindexed, and have no duplicates
# written with {}

fruits = {"apple", "banana", "cherry"}
print(fruits)

# No duplicates allowed
fruits = {"apple", "banana", "apple"}
print(fruits)

# check to see if item exists
print("banana" in fruits)

# Adding items 
fruits.update(["kiwi", "mango"])
print(fruits)

# Remove items
fruits.remove("kiwi")
print(fruits)

# Set operation
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

#print(set1.union(set2)) # combines both (no duplicates)
##print(set1.intersection(set2)) # combines duplicates as new sets 
print(set1.difference(set2)) #  what only in set 1 



invited_friends = {"Alex", "Sam", "Leo", "Nina"}
rsvped = {"Nina", "Sam", "Jordan"}

print(invited_friends.union(rsvped)) 
print(invited_friends.intersection(rsvped)) 
print(invited_friends.difference(rsvped)) 

invited_friends.update(["Luke", "Turtle"])
print(invited_friends)

rsvped.remove("Sam")
print(rsvped)

total_guest = (invited_friends, rsvped)
print(len(total_guest))

if "Leo" in invited_friends:
    print("Naw bro to cool for school")