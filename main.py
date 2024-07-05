import random
import string


def generate_password(length):
    """Generate a random password of a given length."""
    if length < 4:
        raise ValueError("Password length should be at least 4")

    # Character sets to use in the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with random choices from all sets
    all_chars = lower + upper + digits + special
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the generated password list to avoid predictable sequences
    random.shuffle(password)

    # Join the list to form the final password string
    return ''.join(password)


def generate_passwords(length, count):
    """Generate a list of random passwords."""
    return [generate_password(length) for _ in range(count)]


if __name__ == "__main__":
    print("Welcome to the Secure Password Generator!")
    try:
        length = int(input("Enter the desired password length: "))
        count = int(input("Enter the number of passwords to generate: "))
        passwords = generate_passwords(length, count)
        print("\nGenerated Passwords:")
        for pwd in passwords:
            print(pwd)
    except ValueError as e:
        print(f"Error: {e}")

