import json
import os 


class StudentManager:
    def __init__(self, data_file="/app/data/students.json"):
        self.data_file = data_file
        self.students = []
        self.load_students()
    
    def load_students(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                self.students = json.load(f)
        else:
            self.students = [] 

    def save_students(self):
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        with open(self.data_file, "w") as f:
            json.dump(self.students, f, indent=4)   
        
    def add_student(self, name, age):
        self.students.append({"name": name, "age": age})
        self.save_students()
        print(f"Student '{name}' added successfully!")

    def list_students(self):
        if not self.students:
            print("No students found.")
        else:
            print("\nList of Students:")
            for idx, student in enumerate(self.students, start=1):
                print(f"{idx}. {student['name']} (Age: {student['age']})")
