import random
import string

lower_case = input("Do you want your password with lower case ? (yes/no): ").lower()
upper_case = input("Do you want your password with upper case ? (yes/no): ").lower()
spcl_char = input("Do you want your password with some special characters ? (yes/no): ").lower()
numbers = input("Do you want your password with numbers ? (yes/no): ").lower()

pass_len = int(input("how long are you expecting your password to be ?: "))
all_char = ''

if lower_case == 'yes':
    all_char += string.ascii_lowercase

if upper_case == 'yes':
    all_char += string.ascii_uppercase

if spcl_char == 'yes':
    all_char += string.punctuation

if numbers == 'yes':
    all_char += string.digits

if all_char == '':
    print("You need to include at least one type of character to generate a password.")
else:
    password = ''
    for i in range(pass_len):
        rand_tot_char = random.choice(all_char)
        password += rand_tot_char
    print("Your generated password is: ",password)