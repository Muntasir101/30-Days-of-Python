import random


# function to generate a user ID
def generate_user_id():
    user_ids = ""
    for i in range(6):
        user_ids += random.choice("abcdefghijklmnopqrstuvwxyz0123456789")
    return user_ids


# function to generate a password
def generate_password():
    passwords = ""
    for i in range(8):
        passwords += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*")
    return passwords


# generate user ID and password
user_id = generate_user_id()
password = generate_password()

# print user ID and password
print("User ID:", user_id)
print("Password:", password)
