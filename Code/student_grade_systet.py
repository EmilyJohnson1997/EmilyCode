# student_grade_system.py
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

if __name__ == "__main__":
    students = [
        Student("Alice", [85, 92, 78]),
        Student("Bob", [79, 95, 88]),
        Student("Charlie", [92, 87, 90])
    ]

    for student in students:
        print(f"{student.name}'s average grade: {student.average_grade():.2f}")
        print("777")
