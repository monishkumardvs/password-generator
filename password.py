import secrets
import string
import random

def generate_password(length):
    """
    Generate a secure random password with the specified length.
    :param length: Length of the password.
    :return: Secure random password.
    """
    characters = string.ascii_lowercase + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length - 2))
    password += secrets.choice(string.ascii_uppercase)  # Add at least one uppercase letter
    password += secrets.choice(string.digits)  # Add at least one digit
    password += secrets.choice(string.punctuation)  # Add one special character
    password_list = list(password)
    random.shuffle(password_list)  # Shuffle the password characters
    return ''.join(password_list)

def generate_multiple_passwords(num_passwords, length):
    """
    Generate multiple secure random passwords.
    :param num_passwords: Number of passwords to generate.
    :param length: Length of each password.
    :return: List of secure random passwords.
    """
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

# Get user input for the number of passwords and length
num_passwords = int(input("How many passwords do you want to generate? "))
password_length = int(input("Enter the desired length for each password (minimum 5): "))

# Generate passwords
generated_passwords = generate_multiple_passwords(num_passwords, max(5, password_length))

# Display the generated passwords
print("\nGenerated Passwords:")
for password in generated_passwords:
    print(password)
