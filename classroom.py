class student:
    def __init__(self, name, grade, school):
        self.name = name
        self.grade = grade
        self.school = school

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Grade: {self.name}")
        print(f"School: {self.school}")

student1 = student("Sam", "11th", "California High School")

student1.display_info()