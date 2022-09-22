"""
Password stars
A program to print a star for every character in password.
"""
MINIMUM_PASSWORD_LENGTH = 8

password = input("Enter password: ")
while len(password) < MINIMUM_PASSWORD_LENGTH:
    print("Password is too short.")
    password = input("Enter password: ")
print("*" * len(password))
