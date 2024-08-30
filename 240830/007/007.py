class Test:
    def __init__(self, secKey, location, hour):
        self.secKey = secKey
        self.location = location
        self.hour = hour

    def __str__(self):
        return '''secret code : {a}
meeting point : {b}
time : {c}'''.format(a=self.secKey, b=self.location, c=self.hour)

a, b, c = input().split()

test = Test(a, b, c)

print(test)