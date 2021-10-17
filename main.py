#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_numbers = []
for number in range(0, nr_numbers):
  number = random.randint(0, nr_numbers)
  password_numbers += str(number)
# print(password_numbers)

password_letters = []
for number in range(0, nr_letters):
  number = letters[int(random.random() * len(letters))]
  password_letters += str(number)
# print(password_letters)

password_symbols = []
for number in range(0, nr_symbols):
  number = symbols[int(random.random() * len(symbols))]
  password_symbols += str(number)
# print(password_symbols)

password = password_numbers + password_letters + password_symbols

string_password = ""
for number in range(0, len(password)):
  string_password += str(password[number])

#password before the shuffle
# print("Password without randomization")
# print(string_password + "\n")
random.shuffle(password)

string_password = ""
for number in range(0, len(password)):
  string_password += str(password[number])

#password after the shuffle
# print("Password with random selection")
print(string_password)
