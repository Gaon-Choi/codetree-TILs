def print_symmetric(n):
    if n == 0:
        return
    else:
        print(n, end=" ")
        print_symmetric(n - 1)
        print(n, end=" ")

N = int(input())
print_symmetric(N)