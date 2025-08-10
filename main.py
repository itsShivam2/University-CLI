from student_manager import StudentManager

def main():
    manager = StudentManager()

    while True:
        print("Welcome to the University Management System! 🎓")
        print("1. Add Student")
        print("2. List Students")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            manager.add_student(name, age)
        elif choice == "2":
            manager.list_students()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
