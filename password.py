from hashlib import new
import random
import string

numbers = string.digits
symbol = string.punctuation
lower_case = string.ascii_lowercase
big_case = string.ascii_uppercase
characters = [numbers,symbol,lower_case,big_case]




password = ""

for i in range(2):
    password += characters[0][random.randint(0,9)]
for i in range(2):
    password += characters[1][random.randint(0,9)]
for i in range(2):
    password += characters[2][random.randint(0,9)]
for i in range(2):
    password += characters[3][random.randint(0,9)]

for j in range(4):
    for i in range(2):
        password += characters[j][random.randint(0,9)]


password += numbers[random.randint(0,9)]
password += numbers[random.randint(0,9)]

print(password)
password = list(password)
random.shuffle(password)
print(password)

new_password = ""
new_password = new_password.join(password)

print(new_password)
