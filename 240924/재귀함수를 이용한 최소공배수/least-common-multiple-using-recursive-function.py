def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def lcm_recursive(num_list: list):
    if len(num_list) == 2:
        return lcm(num_list[0], num_list[1])
    elif len(num_list) == 1:
        return num_list[0]
    else:
        return lcm(num_list[0], lcm_recursive(num_list[1:]))

N = int(input())

arr = list(map(int, input().split()))

print(lcm_recursive(arr))