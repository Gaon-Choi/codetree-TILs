class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def __str__(self):
        return "{name} {height} {weight}".format(name=self.name, height=self.height, weight=self.weight)

n = int(input())

persons = []

for _ in range(n):
    persons.append(Person(*input().split()))

persons = sorted(persons, key= lambda x: int(x.height))

for person in persons:
    print(person)