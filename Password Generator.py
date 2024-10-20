import random
import string

def generate_password():
    print("🔒 Hey, Welcome to the Ultimate Password Generator! 🔒")
    
    while True:
        try:
            length = int(input("\nPlease Enter the desired password length (minimum 6 characters): "))
            if length < 6:
                print("Oops! Sorry the Password length is too short! Please choose a length of at-least 6.")
            else:
                break
        except ValueError:
            print("uff!! Invalid input! Please enter a valid number.")
    
    print("\nNow It's Time to Choose the complexity level:")
    print("1. Only letters! (lowercase and uppercase)")
    print("2. Letters and numbers!")
    print("3. Letters, numbers, and special characters!")
    
    while True:
        complexity = input("\nNow, Enter your choice (1/2/3): ")
        if complexity not in ['1', '2', '3']:
            print("Sorry It's Invalid choice! Please select from options 1, 2, or 3.")
        else:
            break
    
    if complexity == '1':
        characters = string.ascii_letters
        description = "letters only"
    elif complexity == '2':
        characters = string.ascii_letters + string.digits
        description = "letters and numbers"
    elif complexity == '3':
        characters = string.ascii_letters + string.digits + string.punctuation
        description = "letters, numbers, and special characters is"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    print(f"\n✅ Password generated with {description}:")
    print(f"🔑Wow, Your secure password is: '-{password}-'")
    print("💡 Tip: Keep it safe and never share it with anyone!")

generate_password()