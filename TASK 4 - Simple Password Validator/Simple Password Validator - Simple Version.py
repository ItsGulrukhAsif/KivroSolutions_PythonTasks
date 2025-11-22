# Task 4 - Simple Password Validator

def is_valid_password(password):
    # Condition A: Minimum length
    if len(password) < 6:
        return False
    
    # Condition B: Contains at least one digit
    has_number = any(char.isdigit() for char in password)
    
    # Condition C: Contains at least one uppercase letter
    has_capital = any(char.isupper() for char in password)

    return has_number and has_capital


def main():
    while True:
        print("\n===== Password Validator =====")
        password = input("Enter password to validate: ")

        if is_valid_password(password):
            print("✔ Password Accepted\n")
        else:
            print("❌ Password Invalid\n")

        choice = input("Do you want to try again? : ").lower()
        if choice != 'y':
            print("👋 Exiting Password Validator. Goodbye!")
            break


if __name__ == "__main__":
    main()
