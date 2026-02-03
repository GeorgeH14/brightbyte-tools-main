import sys
import random
import string
# Generate Funtion
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# get command line arguments
if len(sys.argv) < 2:
    # no value, so ask for one
    print("--- Simple Password Generator ---")
    size = int(input("Enter password length: "))
else:
    # the size has been provided
    size = int(sys.argv[1])

new_password = generate_password()
print(f"Your new password is: {new_password}")