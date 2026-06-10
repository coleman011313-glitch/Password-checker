password = input("Enter password: ")

if len(password) < 8:
    print("Too short")

elif not any(char.isdigit() for char in password):
    print("Needs a number")

elif not any(char.isupper() for char in password):
    print("Password needs uppercase")

else:
    print("Password OK")
