student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}


def average(sequence):
    return sum(sequence) / len(sequence)


print(average(student["grades"]))
#print(student.average())


class Student:
    def __init__(self):
        self.name = "Rolf"
        self.grades = (90, 90, 93, 78, 90)

    def average_grades(self):
        return sum(self.grades) / len(self.grades)


student = Student()
print(student.name)
print(student.grades)
print(average(student.grades))

print(student.average_grades())
print(Student.average_grades(student))

print()


class Student1:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grades(self):
        return sum(self.grades) / len(self.grades)


student = Student1("Bob", (100, 100, 93, 78, 90))
print(student.name)
print(student.average_grades())

student2 = Student1("Rolf", (90, 90, 93, 78, 90))
print(student2.name)
print(student2.average_grades())


