class Student:
    def __init__(self, number, height, weight):
        self.number = int(number)
        self.height = int(height)
        self.weight = int(weight)

    def __str__(self):
        return "{height} {weight} {number}".format(height=self.height, weight=self.weight, number=self.number)

N = int(input())

students = []

for i in range(N):
    students.append(Student(i + 1, *input().split()))

students.sort(key = lambda student : (-student.height, -student.weight, student.number))

for student in students:
    print(student)