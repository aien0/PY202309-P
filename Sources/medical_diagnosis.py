import csv

class MedicalDiagnosis:
    def __init__(self, csv_path):
        self.data = self.load_data(csv_path)
        self.user_input = {}
        self.matched_patients = []

    def load_data(self, csv_path):
        try:
            with open(csv_path, 'r') as csvfile:
                reader = csv.reader(csvfile)
                header = next(reader)  # 첫 행을 헤더로 읽음
                data = [row for row in reader]
                return {'header': header, 'data': data}
        except Exception as e:
            print(f"Error loading data from CSV: {e}")
            return {'header': [], 'data': []}
        

    def calculate_similarity_score(self, patient):
        return sum([1 for i, value in enumerate(patient) if i in self.data['header'] and self.user_input.get(self.data['header'][i]) == value])


    def find_similar_disease(self):
        # 사용자 입력과 CSV 데이터를 비교하여 유사한 환자의 질병을 찾는다
        if not self.matched_patients:
            print("유사한 환자가 없습니다. 병원을 찾아주세요.")
            return

        # 가장 유사한 환자 중 한 명의 데이터를 가져옴 (일단 첫 번째 환자를 사용)
        similar_patient_data = self.matched_patients[0]

        # 환자의 각 항목에 대해 입력값과 비교하여 유사한지 확인
        similar_disease = None
        for key, value in self.user_input.items():
            if similar_patient_data[self.data['header'].index(key)] != value:
                similar_disease = "Unknown"  # 유사한 질병이 없는 경우
                break

        if similar_disease is None:
            # 유사한 질병을 찾았을 경우
            similar_disease = similar_patient_data[self.data['header'].index('Disease')]

        print(f"가장 유사한 환자의 질병은 {similar_disease}입니다.")

    def recommend_hospital(self):
        # 병원 추천 로직 추가
        pass
