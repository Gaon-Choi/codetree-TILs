class User:
    def __init__(self, name, address, city):
        self.name = name
        self.address = address
        self.city = city

    def __str__(self):
        return '''name {name}
addr {addr}
city {city}'''.format(name=self.name, addr=self.address, city=self.city)

n = int(input())

users = []

for _ in range(n):
    users.append(User(*input().split()))

users = sorted(users, key=lambda user: user.name, reverse=True)

print(users[0])