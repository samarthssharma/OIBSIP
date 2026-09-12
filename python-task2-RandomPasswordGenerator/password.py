import random
import string

print("Welcome to the Random Password Generator")
print("----------------------------------------")

while True:
    # 1. Get password length from the user
    length_input = input("\nHow long do you want the password to be? (minimum 8): ")
    
    # Validation: Check if it's a number and at least 8
    try:
        length = int(length_input)
        if length < 8:
            print("Error: Password must be at least 8 characters long.")
            continue # This sends them back to the start of the loop
    except ValueError:
        print("Error: Please enter a valid number.")
        continue

    # 2. Ask which character types to include
    print("\nPlease answer 'yes' or 'no' for the following:")
    use_upper = input("Include uppercase letters? ").strip().lower()
    use_lower = input("Include lowercase letters? ").strip().lower()
    use_numbers = input("Include numbers? ").strip().lower()
    use_symbols = input("Include symbols? ").strip().lower()

    # 3. Figure out how many types were selected and build the character pool
    types_selected = 0
    allowed_chars = ""

    if use_upper == 'yes':
        types_selected = types_selected + 1
        allowed_chars = allowed_chars + string.ascii_uppercase
        
    if use_lower == 'yes':
        types_selected = types_selected + 1
        allowed_chars = allowed_chars + string.ascii_lowercase
        
    if use_numbers == 'yes':
        types_selected = types_selected + 1
        allowed_chars = allowed_chars + string.digits
        
    if use_symbols == 'yes':
        types_selected = types_selected + 1
        allowed_chars = allowed_chars + string.punctuation

    # Validation: Check if at least 2 types were selected
    if types_selected < 2:
        print("Error: You must select at least 2 types of characters. Let's try again.")
        continue

    # 4. Generate the password
    password = ""
    for i in range(length):
        # Pick a random character from our allowed pool and add it to the password
        random_char = random.choice(allowed_chars)
        password = password + random_char

    # 5. Display the result
    print("\n--- Your New Password ---")
    print(password)
    print("-------------------------")

    # 6. Option to generate another one without restarting
    again = input("\nDo you want to generate another password? (yes/no): ").strip().lower()
    if again != 'yes':
        print("Thank you for using the generator. Goodbye!")
        break