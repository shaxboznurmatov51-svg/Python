# 1. Write a Python script to sort (ascending and descending) a dictionary by value.
d = {1: 2, 3: 1, 2: 3}
# Ascending
ascending = dict(sorted(d.items(), key=lambda x: x[1]))
print("Ascending:", ascending)
# Descending
descending = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
print("Descending:", descending)

# 2. Write a Python script to add a key to a dictionary.
d = {0: 10, 1: 20}
d[2] = 30
print(d)

# 3. Write a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

new_dict = {}
new_dict.update(dic1)
new_dict.update(dic2)
new_dict.update(dic3)

# 4. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n = 5
d = {}
for x in range(1, n+1):
    d[x] = x * x
print(d)

# 5. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) 
# and the values are the square of the keys.
d = {x: x*x for x in range(1, 15+1)}
print(d)

# 1. Write a Python program to create a set.
my_set = {1, 2, 3}
print(my_set)

# 2. Iterate Over a Set
my_set = {"apple", "banana", "cherry"}
for item in my_set:
    print(item)

# 3. Write a Python program to add member(s) to a set.
my_set = {1, 2, 3}
my_set.add(4)
my_set.update([5, 6])
print(my_set)

# 4. Write a Python program to remove item(s) from a given set.
my_set.remove(3) # removes 3
my_set.discard(7) # no error if not exist
print(my_set)

# 5. Write a Python program to remove an item from a set if it is present in the set.
my_set = {1, 2, 3}
item = 2
if item in my_set:
    my_set.remove(item)
    print(f"{item} is removed")
else:
     print(f"{item} does not exists")























