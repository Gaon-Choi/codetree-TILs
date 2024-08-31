def one_to_n(n):
    if n == 0:
        return
    else:
        one_to_n(n - 1)
        print(n, " ", sep="", end='')

def n_to_one(n):
    if n == 0:
        return
    else:
        print(n, " ", sep="", end='')
        n_to_one(n - 1)

n = int(input())

one_to_n(n)
print()
n_to_one(n)