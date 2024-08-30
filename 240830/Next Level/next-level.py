class Test:
    def __init__(self, ID, level):
        self.ID = ID
        self.level = level

    def __str__(self):
        return '''user {ID} lv {lv}'''.format(ID=self.ID, lv=self.level)

ID, level = input().split()

test1 = Test("codetree", 10)
test2 = Test(ID, level)

print(test1)
print(test2)