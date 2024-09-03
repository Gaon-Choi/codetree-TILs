import math

class User:
    def __init__(self, name, score):
        self.name = name
        self.score = score

users = []

for _ in range(5):
    name, score = input().split()
    users.append(User(name, int(score)))

minima_name = ""
minima_score = math.inf

for elem in users:
    if minima_score > elem.score:
        minima_score = elem.score
        minima_name = elem.name

print(minima_name, minima_score)