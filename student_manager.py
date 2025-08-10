class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, age):
        self.students.append({"name": name, "age": age})
        print(f"Student '{name}' added successfully!")

    def list_students(self):
        if not self.students:
            print("No students found.")
        else:
            print("\nList of Students:")
            for idx, student in enumerate(self.students, start=1):
                print(f"{idx}. {student['name']} (Age: {student['age']})")
