# Tuples are imutable (you can't change them)
# Written using parenthesis ()

my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

# Accessing items
print(my_tuple[0])
print(my_tuple[2])

# check if an item exists
if "banana" in my_tuple:
    print("Yes banana is in tuple")
    
# Lengh of tuple
print(len(my_tuple))

# Single item tuple
# you must add a comma at the end or python wont read it 
single = ("kiwi")
print(type(single)) # string
tuple = ("kiwi",)
print(type(tuple)) # with comma (tuple)

# Nested Tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
combine = ( tuple1, tuple2)
print(combine)


travel_bag = ("shirt", "shorts", "shoes", "suitcase", "food")
print(travel_bag)

print(travel_bag[1])
print(travel_bag[3])

if "shoes" in travel_bag:
    print("You are ready to walk!")

essentials = ("snacks", "movies", "myself")

travel_bag = ("shirt", "shorts", "shoes", "suitcase", "food")
essentials= ("snacks", "movies", "myself")
combine = ( travel_bag, essentials)
print(combine)

final_bag = (travel_bag, essentials)
print(final_bag)
print(len(final_bag))
print(final_bag[-1])




