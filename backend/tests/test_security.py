from security import hash_password, verify_password

password = "Test@123"

# generate a hashed password
hashed_password = hash_password(password)

print("Hashed password:", hashed_password)

# verify password - case 1: correct password
print("Correct password:", verify_password(password, hashed_password))
# verify password - case 2: incorrect password
print("Incorrect password:", verify_password("WrongPassword", hashed_password))