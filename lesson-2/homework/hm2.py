#1.Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
name = input("Enter your name:")
birth_year = int(input("Enter your year of birth:"))
current_year = datetime.now().year
age = current_year - birth_year
print(f"Hello {name}, you are {age} years old.")

#2. Extract car names from the following text:
txt = 'LMaasleitbtui'
car_names = txt[::2]
print(car_names)
car_malibu = txt[1::2]
print(car_malibu)

#3.Extract car names from the following text:
txt = 'MsaatmiazD'
matiz = txt[::2]
print(matiz)
damas = txt[::-2] 
print(damas)

#4.Extract the residence area from the following text:
txt = "I'am John. I am from London"
residence = txt[txt.index("from") + 5:] 
print(residence)

#5. Write a Python program that takes a user input string and prints it in reverse order.
user_input = input("Enter a string:")
reversed_string = user_input[::-1]
print('Reversed string:', reversed_string)

#6. Write a Python program that counts the number of vowels in a given string.
text = input("Enter a string:")
vowels = 'aeiouAEIOU'
count = sum(1 for char in text if char in vowels)
print(f"Number of vowels: {count}")

# 7. Write a Python program that takes a list of numbers as input and prints the maximum value.
numbers = list(map(int, input("Enter numbers separated by spaces:")))
max_value = max(numbers)
print("Maximum value:", max_value)

# 8. Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
word = input("Enter a word")
if word == word[::-1]:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")

# 9. Write a Python program that extracts and prints the domain from an email address provided by the user.
email = input("Enter your email:")
domain = email.split('@')[-1] 
print("Domain:", domain)

#task 10
import random
import string
length = int(input("Enter password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Generated password:", password)


















