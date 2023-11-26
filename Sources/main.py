from medical_diagnosis import MedicalDiagnosis
from user_input_validator import (
    validate_yes_no_input,
    validate_integer_input,
    validate_gender_input,
)

if __name__ == "__main__":
    csv_path = "C:/Users/82102/Desktop/PY202309-P/Sources/disease_symptom.csv"
    medical_diagnosis = MedicalDiagnosis(csv_path)

    # 사용자에게 8가지 항목을 입력 받음
    Fever = validate_yes_no_input("발열이 있나요? (Yes/No) :")
    Cough = validate_yes_no_input("기침이 있나요? (Yes/No) :")
    Fatigue = validate_yes_no_input("피로감이 있나요? (Yes/No) :")
    Difficulty_Breathing = validate_yes_no_input("호흡 곤란이 있나요? (Yes/No) :")

    Age = validate_integer_input("나이를 입력하세요. :")

    Gender = validate_gender_input("성별을 입력하세요. (Male/Female) :")

    Blood_Pressure = validate_integer_input("수축기 혈압을 입력하세요. :")
    Cholesterol_Level = validate_integer_input("총 콜레스테롤 수치를 입력하세요. :")

    medical_diagnosis.user_input = {
        'Fever': Fever,
        'Cough': Cough,
        'Fatigue': Fatigue,
        'Difficulty Breathing': Difficulty_Breathing,
        'Age': Age,
        'Gender': Gender,
        'Blood Pressure': Blood_Pressure,
        'Cholesterol Level': Cholesterol_Level,
    }


    # 사용자 입력에 기반하여 유사한 환자를 식별함
    medical_diagnosis.find_similar_disease()

    if medical_diagnosis.matched_patients:
        medical_diagnosis.find_similar_disease()
    else:
        print("유사한 환자가 없습니다.")