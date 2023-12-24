from medical_diagnosis import MedicalDiagnosis
from user_input_validator import (
    validate_yes_no_input,
    validate_integer_input,
    validate_gender_input,
)

if __name__ == "__main__":
    # Eight items are entered by the user
    Fever = validate_yes_no_input("발열이 있나요? (Yes/No): ")
    Cough = validate_yes_no_input("기침이 있나요? (Yes/No): ")
    Fatigue = validate_yes_no_input("피로감이 있나요? (Yes/No): ")
    Difficulty_Breathing = validate_yes_no_input("호흡 곤란이 있나요? (Yes/No): ")

    Age = validate_integer_input("나이를 입력하세요: ")

    Gender = validate_gender_input("성별을 입력하세요 (Male/Female): ")

    Blood_Pressure_int = validate_integer_input("수축기 혈압을 입력하세요: ")
    Cholesterol_Level_int = validate_integer_input("총 콜레스테롤 수치를 입력하세요: ")

    def convert_blood_pressure(value): # systolic blood pressure
        if value <= 90:
            return "Low" # low blood pressure
        elif 90 < value <= 120:
            return "Normal"
        else:
            return "High" # High blood pressure

    def convert_cholesterol_level(value): # total cholesterol level
        if value < 140:
            return "Low"
        elif 140 <= value <= 200:
            return "Normal"
        else:
            return "High"
        
    # Conversion of blood pressure and cholesterol levels (range)
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

    # Top-3 Diseases
    print("Top-3 Diseases:")
    for disease, similarity, probability in top_diseases:
        print(f"{disease}: Similarity - {similarity}, Probability - {probability}%")
    
    recommended_hospitals = diagnosis.recommend_hospital(top_diseases)

    # Recommended Hospitals
    print("\nRecommended Hospitals:")
    for disease, hospital, probability in recommended_hospitals:
        print(f"For {disease}, Recommended Hospital: {hospital}")
