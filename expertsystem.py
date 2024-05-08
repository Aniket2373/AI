from datetime import datetime
from pickle import TRUE

class hospitalexpertsytem:

    def _init_(self):
        self.reset()
        self.patient_info={}

    def reset(self):
        self.hospital={"temp":None,"cough":False,"sore_throat":False}
        self.patient_info={}

    def setdata(self,key,value):
        self.hospital[key]=value

    def set_patient_info(self):
        self.patient_info['name']=input("name : ")
        self.patient_info['gender']=input("gender : ")
        self.patient_info['age']=input("age : ")

    def store_patient_info(self):
        with open("pat.txt",'a')as f:
            f.write(f"Name: {self.patient_info['name']}\n")
            f.write(f"gender: {self.patient_info['gender']}\n")
            f.write(f"age: {self.patient_info['age']}\n")
            f.write(f"diagnosis: {dia}\n")
            f.write(f"treatment: {treat}\n")

    def get_diagnosis(self):
        diagnosis=""
        treatment=""
        medicine=""

        if self.hospital['temp'] == 'high' and self.hospital['cough'] and self.hospital['sore_throat']:
            diagnosis = "Flu"
            treatment = "Rest, fluids, antiviral medication"
            medicine = "Tamiflu (tablets) and Acetaminophen syrup (liquid)"

        elif self.hospital['temp'] == 'high' and not self.hospital['cough'] and not self.hospital['sore_throat']:
            diagnosis = "Fever"
            treatment = "Rest, fluids, fever-reducing medication"
            medicine = "Ibuprofen tablets and Acetaminophen syrup (liquid)"
        
        elif self.hospital['temp'] == 'high' and self.hospital['abdominal_pain']:
            diagnosis = "Typhoid"
            treatment = "Seek medical attention immediately, antibiotics are necessary"
            medicine = "Ciprofloxacin and Azithromycin tablets"
            
        elif self.hospital['temp'] == 'normal' and not self.hospital['cough'] and self.hospital['sore_throat']:
            diagnosis = "Strep throat"
            treatment = "Consult a doctor, antibiotics may be needed"
            medicine = "Penicillin V tablets and Amoxicillin tablets"
        
        elif self.hospital['temp'] == 'high' and self.hospital['headache']:
            diagnosis = "Malaria"
            treatment = "Seek medical attention immediately, antimalarial drugs are necessary"
            medicine = "Chloroquine tablets and Artemisinin-based combination therapy"
        
        elif self.hospital['temp'] == 'normal' and self.hospital['cough'] and self.hospital['sore_throat']:
            diagnosis = "Common cold"
            treatment = "Rest, fluids, over-the-counter cold medication"
            medicine = "DayQuil (tablets) and NyQuil syrup (liquid)"

        elif self.hospital['temp'] == 'normal' and (self.hospital['rash'] or self.hospital['itching']):
            diagnosis = "Allergies"
            treatment = "Avoid allergens, antihistamines may help"
            medicine = "Cetirizine tablets and Loratadine tablets"
          
        else:
            diagnosis="no "
            treatment="no "
            medicine=" no "

        return  diagnosis,treatment,medicine
    

if __name__ == "__main__":

    while TRUE:
        obj=hospitalexpertsytem()

        obj.reset()
        obj.set_patient_info()
        obj.setdata("temp",input("enter temp :"))
        obj.setdata('cough', input("Do you have a cough? (yes/no): ").lower() == 'yes')
        obj.setdata('sore_throat', input("Do you have a sore throat? (yes/no): ").lower() == 'yes')
        if obj.hospital['temp'] == 'high':
            obj.setdata('headache', input("Do you have a headache? (yes/no): ").lower() == 'yes')
            obj.setdata('abdominal_pain', input("Do you have abdominal pain? (yes/no): ").lower() == 'yes')
        else:
            obj.setdata('rash', input("Do you have a rash? (yes/no): ").lower() == 'yes')

        dia,treat,med=obj.get_diagnosis()
        print("\n")
        print("Diagnosis: ",dia)
        print("Treatment: ",treat)
        print("Suggested medicine: ",med)
        obj.store_patient_info()
        print("get well soon ")