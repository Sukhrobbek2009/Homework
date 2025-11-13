class student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        average = sum(self.grades) / len(self.grades)
        print(f"{self.name}'s average grade is : {average:2f}")