class Bomb:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

    def __str__(self):
        return '''code : {code}
color : {color}
second : {second}'''.format(code=code, color=color, second=second)

code, color, second = input().split()
second = int(second)

bomb = Bomb(code, color, second)

print(bomb)