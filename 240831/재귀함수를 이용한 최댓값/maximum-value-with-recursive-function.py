def select_max_recursive(num_list: list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return select_max_recursive([max(num_list[0], num_list[1])] + num_list[2:])

N = int(input())
num_list = list(map(int, input().split()))
maxima = select_max_recursive(num_list)

print(maxima)