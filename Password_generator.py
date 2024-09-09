import random
import string

def generate_pwd(min_length, numbers=True, special_char=True):
    letters = string.ascii_letters
    nums = string.digits
    special_chars = string.punctuation

    pwd_items = letters
    if numbers:
        pwd_items += nums
    if special_char:
        pwd_items += special_chars

    pwd = ""
    meet_criteria = False
    has_num = False
    has_Special = False

    while not meet_criteria or len(pwd) < min_length:
        random_char = random.choice(pwd_items)
        pwd += random_char

        if random_char in nums:
            has_num = True
        if random_char in special_chars:
            has_Special = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_num
        if special_char:
            meet_criteria = meet_criteria and has_Special

    return pwd

min_length = int(input("Enter the minimum length of password: "))
has_number = input("Do you want to have numbers (y/n)?: ").lower() == 'y'
has_special = input("Do you want to have special characters (y/n)?: ").lower() == 'y'
password = generate_pwd(min_length, has_number, has_special)
print("The generated password is:", password)
