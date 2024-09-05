class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = int(height)
        self.weight = int(weight)

    def __str__(self):
        return "{name} {height} {weight}".format(name=self.name, height=self.height, weight=self.weight)

N = int(input())

persons = []

for _ in range(N):
    persons.append(Person(*input().split()))

persons.sort(key = lambda person : (person.height, -person.weight))

for person in persons:
    print(person)