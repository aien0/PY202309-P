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
        # Count the number of matching symptoms and use them as similarities
        similarity = sum(1 for key, value in self.user_input.items() if value == row[key])
        total_symptoms = len(self.user_input)
        probability = (similarity / total_symptoms) * 100
        return similarity, probability

    def find_top_diseases(self, top_n=3):
        similarities = []

        for row in self.data:
            similarity, probability = self.calculate_similarity(row)
            disease_name = row['Disease']
            similarities.append((disease_name, similarity, probability))

        # Sort in descending order by similarity
        similarities.sort(key=lambda x: x[1], reverse=True)

        # Top N disease extraction
        top_diseases = similarities[:top_n]

        return top_diseases
    
    def recommend_hospital(self, top_diseases):
        recommended_hospitals = []

        for disease, similarity, probability in top_diseases:
            hospital_for_disease = self.map_disease_to_hospital(disease)
            recommended_hospitals.append((disease, hospital_for_disease, probability))

        return recommended_hospitals

    def map_disease_to_hospital(self, disease):
        hospital_mapping = {
            'Acne': '피부과',
            'Allergic Rhinitis': '이비인후과',
            'Alzheimer\'s Disease': '신경과',
            'Anemia': '내과',
            'Anxiety Disorders': '정신건강의학과',
            'Appendicitis': '외과',
            'Asthma': '호흡기내과',
            'Atherosclerosis': '순환기내과',
            'Autism Spectrum Disorder (ASD)': '소아청소년과 또는 정신건강의학과',
            'Bipolar Disorder': '정신건강의학과',
            'Bladder Cancer': '비뇨기과',
            'Brain Tumor': '신경외과',
            'Breast Cancer': '외과 또는 유방외과',
            'Bronchitis': '호흡기내과',
            'Cataracts': '안과',
            'Cerebral Palsy': '소아청소년과 또는 재활의학과',
            'Chickenpox': '소아청소년과',
            'Cholecystitis': '외과',
            'Cholera': '감염내과',
            'Chronic Kidney Disease': '신장내과',
            'Chronic Obstructive Pulmonary Disease (COPD)': '호흡기내과',
            'Cirrhosis': '소화기내과',
            'Colorectal Cancer': '소화기외과',
            'Common Cold': '일반 내과',
            'Conjunctivitis (Pink Eye)': '안과',
            'Coronary Artery Disease': '순환기내과',
            'Crohn\'s Disease': '소화기내과',
            'Cystic Fibrosis': '호흡기내과',
            'Dementia': '신경과 또는 정신건강의학과',
            'Dengue Fever': '감염내과',
            'Depression': '정신건강의학과',
            'Diabetes': '내분비내과',
            'Diverticulitis': '소화기내과',
            'Down Syndrome': '소아청소년과',
            'Eating Disorders (Anorexia, ...)': '정신건강의학과 또는 영양과',
            'Ebola Virus': '감염내과',
            'Eczema': '피부과',
            'Endometriosis': '산부인과',
            'Epilepsy': '신경과 또는 소아신경과',
            'Esophageal Cancer': '소화기외과',
            'Fibromyalgia': '리움토이드 내과 또는 물리치료과',
            'Gastroenteritis': '소화기내과',
            'Glaucoma': '안과',
            'Gout': '류마티스내과 또는 정형외과',
            'HIV/AIDS': '감염내과 또는 면역학과',
            'Hemophilia': '혈액종양내과 또는 혈관외과',
            'Hemorrhoids': '외과',
            'Hepatitis': '간내과',
            'Hepatitis B': '간내과',
            'Hyperglycemia': '내분비내과',
            'Hypertension': '순환기내과',
            'Hypertensive Heart Disease': '순환기내과',
            'Hyperthyroidism': '내분비내과',
            'Hypoglycemia': '내분비내과',
            'Hypothyroidism': '내분비내과',
            'Influenza': '감염내과',
            'Kidney Cancer': '종양내과 또는 비뇨기과',
            'Kidney Disease': '비뇨기과 또는 내과',
            'Klinefelter Syndrome': '내분비내과 또는 소아청소년과',
            'Liver Cancer': '종양내과 또는 간외과',
            'Liver Disease': '간내과',
            'Lung Cancer': '종양내과 또는 흉부외과',
            'Lyme Disease': '감염내과 또는 래트로학과',
            'Lymphoma': '혈액종양내과 또는 혈관외과',
            'Malaria': '감염내과',
            'Marfan Syndrome': '내과 또는 소아청소년과',
            'Measles': '소아청소년과',
            'Melanoma': '피부외과 또는 종양내과',
            'Migraine': '신경과 또는 통증의학과',
            'Multiple Sclerosis': '신경과',
            'Mumps': '소아청소년과',
            'Muscular Dystrophy': '신경과 또는 물리치료과',
            'Myocardial Infarction (Heart...)': '응급의료 또는 심장내과',
            'Obsessive-Compulsive Disorder': '정신건강의학과',
            'Osteoarthritis': '정형외과 또는 물리치료과',
            'Osteomyelitis': '정형외과',
            'Osteoporosis': '내과 또는 정형외과',
            'Otitis Media (Ear Infection)': '이비인후과',
            'Ovarian Cancer': '종양내과 또는 산부인과',
            'Pancreatic Cancer': '종양내과 또는 소화기외과',
            'Pancreatitis': '소화기내과',
            "Parkinson's Disease": '신경과',
            'Pneumocystis Pneumonia (PCP)': '호흡기내과',
            'Pneumonia': '호흡기내과',
            'Pneumothorax': '흉부외과',
            'Polio': '소아청소년과',
            'Polycystic Ovary Syndrome (PCOS)': '산부인과 또는 내분비내과',
            'Prader-Willi Syndrome': '소아청소년과 또는 내분비내과',
            'Prostate Cancer': '비뇨기과',
            'Psoriasis': '피부과',
            'Rabies': '감염내과',
            'Rheumatoid Arthritis': '류마티스내과 또는 정형외과',
            'Rubella': '소아청소년과',
            'Schizophrenia': '정신건강의학과',
            'Scoliosis': '정형외과',
            'Sepsis': '응급의료 또는 감염내과',
            'Sickle Cell Anemia': '혈액종양내과 또는 혈관외과',
            'Sinusitis': '이비인후과',
            'Sleep Apnea': '호흡기내과 또는 수면의학과',
            'Spina Bifida': '소아청소년과 또는 신경외과',
            'Stroke': '신경과 또는 신경외과',
            'Systemic Lupus Erythematosus...': '류마티스내과',
            'Testicular Cancer': '비뇨기과 또는 종양내과',
            'Tetanus': '감염내과',
            'Thyroid Cancer': '내분비외과 또는 종양내과',
            'Tonsillitis': '이비인후과',
            'Tourette Syndrome': '신경과 또는 소아신경과',
            'Tuberculosis': '감염내과 또는 호흡기내과',
            'Turner Syndrome': '소아청소년과 또는 내분비내과',
            'Typhoid Fever': '감염내과',
            'Ulcerative Colitis': '소화기내과',
            'Urinary Tract Infection': '비뇨기과',
            'Urinary Tract Infection (UTI)': '비뇨기과',
            'Williams Syndrome': '소아청소년과 또는 심장내과',
            'Zika Virus': '감염내과',
        }

        return hospital_mapping.get(disease, 'Unknown Hospital')
