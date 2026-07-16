import re

class DonorHub:
    def __init__(self):
        self.diseases = [
            "HIV Infection",
            "Hepatitis B or C",
            "Convulsions and Epilepsy",
            "Cardio Vascular Diseases",
            "Schizophrenia",
            "Chronic Liver Disease",
            "Current Fever / Acute Infection",
            "Skin Diseases at donation site",
            "Autoimmune Disorders",
            "Severe Allergic Disorders",
            "Recipients of Transplants",
            "Gonorrhoea, Leprosy, Leishmaniasis, Conjunctivitis (recent)"
        ]
        
    def display_title(self):
        print("=" * 60)
        print("              THE DONOR HUB")
        print("=" * 60)
        print("Welcome to donor hub. Register now and save lives!")
        print()
    
    def get_personal_info(self):
        print("PERSONAL INFORMATION")
        print("-" * 30)
        
        name = input("Enter your full name: ")
        
        while True:
            email = input("Enter your email: ")
            if self.validate_email(email):
                break
            else:
                print("Invalid email format. Please try again.")
        
        while True:
            phone = input("Enter your phone number: ")
            if self.validate_phone(phone):
                break
            else:
                print("Invalid phone number. Please enter 10 digits.")
        
        address = input("Enter your address: ")
        
        while True:
            gender = input("Enter your gender (Male/Female): ").strip().lower()
            if gender in ['male', 'female']:
                break
            else:
                print("Please enter either 'Male' or 'Female'")
        
        while True:
            first_time = input("Is this your first time donating? (Yes/No): ").strip().lower()
            if first_time in ['yes', 'no']:
                break
            else:
                print("Please enter either 'Yes' or 'No'")
        
        return {
            'name': name,
            'email': email,
            'phone': phone,
            'address': address,
            'gender': gender,
            'first_time': first_time
        }
    
    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def validate_phone(self, phone):
        return phone.isdigit() and len(phone) == 10
    
    def get_medical_info(self):
        print("\nMEDICAL INFORMATION")
        print("-" * 30)
        
        while True:
            try:
                age = int(input("Enter your age: "))
                if 18 <= age <= 100:
                    break
                else:
                    print("Age must be between 18 and 100. Please try again.")
            except ValueError:
                print("Please enter a valid number for age.")
        
        while True:
            try:
                weight = float(input("Enter your weight (kg): "))
                if 30 <= weight <= 200:
                    break
                else:
                    print("Weight must be between 30 and 200 kg. Please try again.")
            except ValueError:
                print("Please enter a valid number for weight.")
        
        while True:
            try:
                hemoglobin = float(input("Enter your hemoglobin level (g/dL): "))
                if 5 <= hemoglobin <= 20:
                    break
                else:
                    print("Hemoglobin must be between 5 and 20 g/dL. Please try again.")
            except ValueError:
                print("Please enter a valid number for hemoglobin.")
        
        blood_group = input("Enter your blood group (e.g., A+, O-, AB+, etc.): ").upper()
        
        while True:
            blood_pressure = input("Enter your blood pressure (e.g., 120/80): ")
            if self.validate_blood_pressure(blood_pressure):
                break
            else:
                print("Invalid blood pressure format. Please use format like '120/80'")
        
        return {
            'age': age,
            'weight': weight,
            'hemoglobin': hemoglobin,
            'blood_group': blood_group,
            'blood_pressure': blood_pressure
        }
    
    def validate_blood_pressure(self, bp):
        pattern = r'^\d{2,3}/\d{2,3}$'
        if re.match(pattern, bp):
            systolic, diastolic = map(int, bp.split('/'))
            return 60 <= systolic <= 200 and 40 <= diastolic <= 150
        return False
    
    def get_disease_history(self):
        print("\nMEDICAL HISTORY - Please tick (enter 'yes') for any conditions you have:")
        print("-" * 60)
        
        selected_diseases = []
        for disease in self.diseases:
            while True:
                response = input(f"Do you have {disease}? (Yes/No): ").strip().lower()
                if response in ['yes', 'no']:
                    if response == 'yes':
                        selected_diseases.append(disease)
                    break
                else:
                    print("Please enter either 'Yes' or 'No'")
        
        return selected_diseases
    
    def get_female_specific_info(self):
        print("\nADDITIONAL INFORMATION FOR FEMALE DONORS")
        print("-" * 40)
        
        while True:
            pregnant = input("Are you currently pregnant? (Yes/No): ").strip().lower()
            if pregnant in ['yes', 'no']:
                break
            else:
                print("Please enter either 'Yes' or 'No'")
        
        while True:
            abortion = input("Have you had an abortion in the last 6 months? (Yes/No): ").strip().lower()
            if abortion in ['yes', 'no']:
                break
            else:
                print("Please enter either 'Yes' or 'No'")
        
        while True:
            menstruating = input("Are you currently menstruating? (Yes/No): ").strip().lower()
            if menstruating in ['yes', 'no']:
                break
            else:
                print("Please enter either 'Yes' or 'No'")
        
        return {
            'pregnant': pregnant,
            'abortion': abortion,
            'menstruating': menstruating
        }
    
    def check_eligibility(self, personal_info, medical_info, diseases, female_info=None):
        print("\n" + "=" * 60)
        print("ELIGIBILITY CHECK RESULTS")
        print("=" * 60)
        
        # Age criteria
        age_eligible = False
        if personal_info['first_time'] == 'yes':
            age_eligible = 18 <= medical_info['age'] <= 60
        else:
            age_eligible = 18 <= medical_info['age'] <= 65
        
        # Weight criteria
        weight_eligible = 45 <= medical_info['weight'] <= 80
        
        # Hemoglobin criteria
        hemoglobin_eligible = medical_info['hemoglobin'] >= 12.5
        
        # Blood pressure criteria (approximately 120/80)
        systolic, diastolic = map(int, medical_info['blood_pressure'].split('/'))
        bp_eligible = (100 <= systolic <= 140) and (60 <= diastolic <= 90)
        
        # Disease criteria
        disease_eligible = len(diseases) == 0
        
        # Female-specific criteria
        female_eligible = True
        if personal_info['gender'] == 'female':
            female_eligible = (female_info['pregnant'] == 'no' and 
                             female_info['abortion'] == 'no' and 
                             female_info['menstruating'] == 'no')
        
        # Display criteria check
        print(f"✓ Age check (18-65): {'PASS' if age_eligible else 'FAIL'}")
        print(f"✓ Weight check (45-80 kg): {'PASS' if weight_eligible else 'FAIL'}")
        print(f"✓ Hemoglobin check (≥12.5 g/dL): {'PASS' if hemoglobin_eligible else 'FAIL'}")
        print(f"✓ Blood pressure check (approx 120/80): {'PASS' if bp_eligible else 'FAIL'}")
        print(f"✓ Medical history check (no diseases): {'PASS' if disease_eligible else 'FAIL'}")
        if personal_info['gender'] == 'female':
            print(f"✓ Female-specific criteria: {'PASS' if female_eligible else 'FAIL'}")
        
        # Final eligibility
        if (age_eligible and weight_eligible and hemoglobin_eligible and 
            bp_eligible and disease_eligible and female_eligible):
            print("\n🎉 CONGRATULATIONS! You are ELIGIBLE for blood donation! 🎉")
            return True
        else:
            print("\n❌ Unfortunately, you are NOT ELIGIBLE for blood donation at this time.")
            return False
    
    def display_precautions(self):
        print("\n" + "=" * 60)
        print("IMPORTANT PRECAUTIONS FOR BLOOD DONATION")
        print("=" * 60)
        precautions = [
            "1. The donor shall be in good health, mentally alert and physically fit and shall not be inmates of jail or any other confinement.",
            "2. First time donor shall not be over 60 years of age, for repeat donor upper limit is 65 years.",
            "3. The donor shall not be fasting before the blood donation or observing fast during the period of blood donation and last meal should have been taken at least 4 hours prior to donation.",
            "4. Donor shall not have consumed alcohol and show signs of intoxication before the blood donation. The donor shall not be a person having regular heavy alcohol intake.",
            "5. The donor who works as air crew member, long distance vehicle driver, either above sea level or below sea level or in emergency services or where strenuous work is required, shall not donate blood at least 24 hours prior to their next duty shift. The donor shall not be a night shift workers without adequate sleep."
        ]
        
        for precaution in precautions:
            print(precaution)
    
    def run(self):
        self.display_title()
        
        # Get personal information
        personal_info = self.get_personal_info()
        
        # Get medical information
        medical_info = self.get_medical_info()
        
        # Get disease history
        diseases = self.get_disease_history()
        
        # Get female-specific information if applicable
        female_info = None
        if personal_info['gender'] == 'female':
            female_info = self.get_female_specific_info()
        
        # Check eligibility
        is_eligible = self.check_eligibility(personal_info, medical_info, diseases, female_info)
        
        # Display precautions
        self.display_precautions()
        
        print("\n" + "=" * 60)
        print("Thank you for your interest in saving lives!")
        print("=" * 60)

# Run the program
if __name__ == "__main__":
