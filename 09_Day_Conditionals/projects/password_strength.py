"""
Project: Password Strength Checker

The aim of this project is to build a password strength checker that
assesses the strength of a password based on certain criteria such as
the length, the presence of numbers, special characters, and uppercase letters.
The program should then provide feedback to the user on the strength of their password.
"""


def check_password_strength(password):
    """
    This function checks the strength of a password
    """
    score = 0

    # Check password length
    if len(password) >= 8:
        score += 1

    # Check for uppercase letters
    if any(c.isupper() for c in password):
        score += 1

    # Check for numbers
    if any(c.isdigit() for c in password):
        score += 1

    # Check for special characters
    if any(c in "!@#$%^&*()_+-=[]{}|;':\"<>,./?`~" for c in password):
        score += 1

    # Assign a password strength based on the score
    if score == 0:
        return "Very weak password"
    elif score == 1:
        return "Weak password"
    elif score == 2:
        return "Moderate password"
    elif score == 3:
        return "Strong password"
    elif score == 4:
        return "Very strong password"


# Main function
def main():
    password = input("Enter a password: ")
    strength = check_password_strength(password)
    print(strength)


if __name__ == "__main__":
    main()
