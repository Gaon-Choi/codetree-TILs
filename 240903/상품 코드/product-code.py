class Product:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __str__(self):
        return "product {code} is {name}".format(code=self.code, name=self.name)

name_, code_ = input().split()

p1 = Product("codetree", 50)
p2 = Product(name_, code_)

print(p1)
print(p2)