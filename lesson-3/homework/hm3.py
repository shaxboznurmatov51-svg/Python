# 1. Create a list containing five different fruits and print the third fruit.
my_list = ["orange", "apple", "banana", "grape", "kiwi"]
print("third fruit:", my_list[2])

# 2. Create two lists of numbers and concatenate them into a single list.
list_1 = [1, 3, 5, 7, 9]
list_2 = [2, 4, 6, 8, 10]
combined_list = list_1 + list_2
print("combined_list:", combined_list)

# 3. Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
numbers = [10, 20, 30, 40, 50, 60, 70]
new_list = [numbers[0], numbers[len(numbers)//2], numbers[-1]] 
print("new_list:", new_list)

# 4. Create a list of your five favorite movies and convert it into a tuple.
my_list = ["interstellor", "creed", "John Wick", "Speed", "Network"]
tuple_list = tuple(my_list)
print("five favourite movies:", tuple_list)

# 5. Given a list of cities, check if "Paris" is in the list and print the result.
cities = ["New York", "London", "Paris", "Tashkent"]
if "Paris" in cities:
    print("Paris is in the list")
else:
    print("Paris is not in the list")


# 6. Create a list of numbers and duplicate it without using loops.
numbers = [10, 20, 30, 40, 50]
duplicate = numbers * 2
print("Duplicated list", duplicate)

# 7. Given a list of numbers, swap the first and last elements.
nums = [10, 20, 30, 40, 50]
nums[0], nums[-1] = nums[-1], nums[0]
print("After swapping:", nums)

# Task 8
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Slice from index 3 to 7:", numbers[3:8])

# 9. Create a list of colors and count how many times "blue" appears in the list.
colours = ["blue", "red", "green", "blue"]
counts_blue = colours.count ("blue")
print("Number of counts of blue:", counts_blue)

# 10. Given a tuple of animals, find the index of "lion".
animals = ("tiger", "lion", "monkey", "snake")
ind_lion = animals.index("lion")
print("The index of lion is ", ind_lion)

# 11. Create two tuples of numbers and merge them into a single tuple.
tuple_1 = (1, 2, 3, 4)
tuple_2 = (5, 6, 7, 8)
merged = tuple_1 + tuple_2
print("merged tuple:", merged) 

# 12. Given a list and a tuple, find and print their lengths.
my_list = [10, 20, 30, 40]
my_tuple = (5, 15, 25, 35)
print("Length of list:", len(my_list))
print("Length of tuple:", len(my_tuple))

# 13. Create a tuple of five numbers and convert it into a list.
tuple_list = (1, 2, 3, 4, 5)
new_list =list(tuple_list)
print("converted to list:", new_list)

# 14. Given a tuple of numbers, find and print the maximum and minimum values.
num_tuple = (3, 5, 8, 14, 15, 34 )
print("minimum number:", min(num_tuple))
print("maximum number:", max(num_tuple))

# 15. Create a tuple of words and print it in reverse order.
words = ("hello", "noutbook", "city", "country")
reverse_tuple = words[::-1]
print("reversed tuple:", reverse_tuple)



























