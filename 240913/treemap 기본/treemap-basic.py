# TreeMap
# balanced binary tree
# (key, value) : key를 기준으로 노드의 위치가 결정됨
# insert, delete, find -> O(logN)

from sortedcontainers import SortedDict

n = int(input())

queries = []

sorted_dict = SortedDict()

for _ in range(n):
    queries.append(input().split())

for q in queries:
    if q[0] == "add":
        sorted_dict[int(q[1])] = int(q[2])
    elif q[0] == "find":
        if int(q[1]) in sorted_dict:
            print(sorted_dict[int(q[1])])
        else:
            print("None")
    elif q[0] == "remove":
        sorted_dict.pop(int(q[1]))
    elif q[0] == "print_list":
        if len(sorted_dict) > 0:
            for k in sorted_dict:
                print(sorted_dict[k], end=" ")
            print()
        else:
            print("None")