# Validate and return 'yes' or 'no'
def validate_yes_no_input(message):
    while True:
        user_input = input(f"{message}").lower()
        if user_input in ['yes', 'no']:
            return user_input.capitalize()  # Capitalize and return
            print("올바른 형식으로 입력하세요. 'yes' 또는 'no'로 입력하세요.")

# Validate and return an integer
def validate_integer_input(message):
    while True:
        user_input = input(f"{message}")
        if user_input.isdigit():
            return int(user_input)
        else:
            print("숫자 형식으로 입력하세요.")

# Validate and return 'male' or 'female' 
def validate_gender_input(message):
    while True:
        user_input = input(f"{message}").lower()
        if user_input in ['male', 'female']:
            return user_input.capitalize()  # Capitalize and return
        else:
            print("올바른 형식으로 입력하세요. 'male' 또는 'female'로 입력하세요.")
