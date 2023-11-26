# Yes 또는 No로 응답을 입력받는 함수
def validate_yes_no_input(message):
    while True:
        user_input = input(f"{message}").lower()
        if user_input in ['yes', 'no']:
            return user_input
        else:
            print("올바른 형식으로 입력하세요. 'Yes' 또는 'No'로 입력하세요.")

# 정수 입력 받는 함수
def validate_integer_input(message):
    while True:
        user_input = input(f"{message}")
        if user_input.isdigit():
            return int(user_input)
        else:
            print("숫자 형식으로 입력하세요.")

# 성별 유효성 확인 함수    
def validate_gender_input(message):
    while True:
        user_input = input(f"{message}").lower()
        if user_input in ['male', 'female']:
            return user_input
        else:
            print("올바른 형식으로 입력하세요. 'Male' 또는 'Female'로 입력하세요.")
