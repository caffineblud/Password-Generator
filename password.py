import random
import string


def generate_password(length: int = 8) -> str:
    """Generate a random password with uppercase, lowercase, digits, and special characters."""
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")

    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    all_chars = string.ascii_letters + string.digits + string.punctuation
    remaining = [random.choice(all_chars) for _ in range(length - 4)]

    password_chars = [upper, lower, digit, special] + remaining
    random.shuffle(password_chars)
    return "".join(password_chars)


def password_strength(password: str) -> str:
    """Evaluate password strength based on length and character variety."""
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak"
    if score == 3:
        return "Moderate"
    if score >= 4:
        return "Strong"

    return "Unknown"


def show_menu() -> None:
    """Display the menu and handle user choices."""
    while True:
        print("\n=== Password Tool Menu ===")
        print("1. Generate password")
        print("2. Check password strength")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            password = generate_password(8)
            print(f"Generated password: {password}")
        elif choice == "2":
            password = input("Enter password to evaluate: ")
            strength = password_strength(password)
            print(f"Password strength: {strength}")
        elif choice == "3":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    show_menu()
