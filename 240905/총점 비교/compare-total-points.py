class Person:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = int(kor)
        self.eng = int(eng)
        self.math = int(math)

    def __str__(self):
        return "{name} {kor} {eng} {math}".format(name=self.name, kor=self.kor, eng=self.eng, math=self.math)

n = int(input())

persons = []

for _ in range(n):
    persons.append(Person(*input().split()))

persons = sorted(persons, key = lambda person : person.kor + person.eng + person.math)

for person in persons:
    print(person)