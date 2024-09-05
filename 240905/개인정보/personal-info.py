class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = int(height)
        self.weight = float(weight)

    def __str__(self):
        return "{name} {height} {weight:.1f}".format(name=self.name, height=self.height, weight=self.weight)

persons = []

for _ in range(5):
    persons.append(Person(*input().split()))

sort_by_name = sorted(persons, key= lambda person : person.name)
sort_by_height = sorted(persons, key= lambda person : -person.height)

print("name")
for person in sort_by_name:
    print(person)

print()
print("height")
for person in sort_by_height:
    print(person)