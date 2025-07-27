import random
import string

# Define character pool: letters, digits, symbols
character_string = string.ascii_letters + string.digits + "!@#$%^&*()"

def generate_password():
    try:
        repeat = int(input("Allow character repetition? (1 = Yes, 0 = No): "))
        length = int(input("Enter desired password length: "))
    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")
        return

    if repeat not in (0, 1):
        print("❌ Invalid option for repetition. Use 1 (Yes) or 0 (No).")
        return

    if length <= 0:
        print("❌ Password length must be greater than 0.")
        return

    if repeat == 0 and length > len(character_string):
        print(f"❌ Cannot create password of length {length} without repeating characters. Max unique characters: {len(character_string)}.")
        return

    if repeat == 1:
        password_chars = random.choices(character_string, k=length)
    else:
        password_chars = random.sample(character_string, length)

    password = ''.join(password_chars)
    print("✅ Generated Password:", password)

# Run the generator
generate_password()
