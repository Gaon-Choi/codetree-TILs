def print_helloworld(n):
    if n == 0:
        return

    else:
        print("HelloWorld")
        return print_helloworld(n-1)

n = int(input())

print_helloworld(n)