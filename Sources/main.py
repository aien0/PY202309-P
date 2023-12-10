from medical_diagnosis import MedicalDiagnosis
from user_input_validator import (
    validate_yes_no_input,
    validate_integer_input,
    validate_gender_input,
)

if __name__ == "__main__":
    # 사용자에게 8가지 항목을 입력 받음
    Fever = validate_yes_no_input("발열이 있나요? (Yes/No): ")
    Cough = validate_yes_no_input("기침이 있나요? (Yes/No): ")
    Fatigue = validate_yes_no_input("피로감이 있나요? (Yes/No): ")
    Difficulty_Breathing = validate_yes_no_input("호흡 곤란이 있나요? (Yes/No): ")

    Age = validate_integer_input("나이를 입력하세요: ")

    Gender = validate_gender_input("성별을 입력하세요 (Male/Female): ")

    Blood_Pressure_int = validate_integer_input("수축기 혈압을 입력하세요: ")
    Cholesterol_Level_int = validate_integer_input("총 콜레스테롤 수치를 입력하세요: ")

    def convert_blood_pressure(value): # 수축기 혈압
        if value <= 90:
            return "Low" # 저혈압
        elif 90 < value <= 120:
            return "Normal"
        else:
            return "High" # 고혈압

    def convert_cholesterol_level(value): # 총 콜레스테롤 수치
        if value < 140:
            return "Low"
        elif 140 <= value <= 200:
            return "Normal"
        else:
            return "High"
        
    # 혈압과 콜레스테롤 수치 변환 (범위로)
    Blood_Pressure = convert_blood_pressure(Blood_Pressure_int)
    Cholesterol_Level = convert_cholesterol_level(Cholesterol_Level_int)
        
    user_input = {
        'Fever': Fever,
        'Cough': Cough,
        'Fatigue': Fatigue,
        'Difficulty Breathing': Difficulty_Breathing,
        'Age': Age,
        'Gender': Gender,
        'Blood Pressure': Blood_Pressure,
        'Cholesterol Level': Cholesterol_Level,
    }

    csv_filename = "C:/Users/82102/Desktop/PY202309-P/Sources/disease_symptom.csv"
    diagnosis = MedicalDiagnosis(user_input, csv_filename)
    diagnosis.load_data()
    top_diseases = diagnosis.find_top_diseases()

    print("Top-3 Diseases:")
    for disease, similarity in top_diseases:
        print(f"{disease}: Similarity - {similarity}")