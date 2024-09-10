def dfs(vertex):
    # adjacent list
    for curr_v in tree[vertex]:
        if not visited[curr_v]:
            parent[curr_v] = vertex
            visited[curr_v] = True
            dfs(curr_v)

n = int(input())

tree = [[] for _ in range(n + 1)]

visited = [False for _ in range(n + 1)]
parent = [-1 for _ in range(n + 1)]

for _ in range(n - 1):
    start, end = map(int, input().split())
    
    tree[start].append(end)
    tree[end].append(start)

dfs(1)

for i in range(2, n + 1):
    print(parent[i])