

import string

COMMON_PASSWORDS = [
    "123456",
    "password",
    "123456789",
    "qwerty",
    "admin",
    "password123"
]


def analyze_password(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("Use at least 12 characters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Add special characters.")

    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback = ["This is a commonly used password."]

    levels = {
        0: "Very Weak",
        1: "Very Weak",
        2: "Weak",
        3: "Moderate",
        4: "Strong",
        5: "Very Strong"
    }

    return levels[score], feedback


def main():
    print("=== PASSWORD STRENGTH ANALYZER ===")

    password = input("Enter a test password: ")

    strength, feedback = analyze_password(password)

    print("\nPassword Strength:", strength)

    if feedback:
        print("\nSuggestions:")
        for suggestion in feedback:
            print("-", suggestion)
    else:
        print("All basic checks passed!")


if __name__ == "__main__":
    main()
