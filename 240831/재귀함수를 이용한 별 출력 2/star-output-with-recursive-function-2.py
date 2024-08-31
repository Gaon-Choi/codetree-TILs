def print_symmetric_star(N: int):
    if N == 0:
        return
    print("* " * N)
    print_symmetric_star(N - 1)
    print("* " * N)

N = int(input())
print_symmetric_star(N)