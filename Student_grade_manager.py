# Student Grade Manager — A Student class storing name, roll number,
# and a list of marks. Add methods to calculate average
# and assign a grade (A/B/C...).
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def calculate_average(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def assign_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def display_student_info(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.calculate_average():.2f}")
        print(f"Grade: {self.assign_grade()}")

s1 = Student("Samyak", 138, [85, 90, 78, 92])
s1.display_student_info()
s2 = Student("Vijay", 139, [75, 80, 68, 72])
s2.display_student_info()
print(f"Average marks of {s1.name} is {s1.calculate_average():.2f} and grade is {s1.assign_grade()}")
print(f"Average marks of {s2.name} is {s2.calculate_average():.2f} and grade is {s2.assign_grade()}")