import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password


print("--- Simple Password Generator ---")
size = int(input("Enter password length: "))

new_password = generate_password(size)
print(f"Your new password is: {new_password}")