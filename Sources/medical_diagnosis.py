import csv

class MedicalDiagnosis:
    def __init__(self, user_input, csv_filename):
        self.user_input = user_input
        self.csv_filename = csv_filename

    def load_data(self):
        with open(self.csv_filename, 'r') as file:
            reader = csv.DictReader(file)
            self.data = list(reader)

    def calculate_similarity(self, row):
        # 일치하는 증상의 개수를 세어 유사도로 사용
        similarity = sum(1 for key, value in self.user_input.items() if value == row[key])
        return similarity

    def find_top_diseases(self, top_n=3):
        similarities = []

        for row in self.data:
            similarity = self.calculate_similarity(row)
            disease_name = row['Disease']
            similarities.append((disease_name, similarity))

        # 유사도를 기준으로 내림차순 정렬
        similarities.sort(key=lambda x: x[1], reverse=True)

        # Top N 질병 추출
        top_diseases = similarities[:top_n]

        return top_diseases
    
    def recommend_hospital(self):
        # 병원 추천 로직 추가
        pass
