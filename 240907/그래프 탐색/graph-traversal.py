def dfs(vertex):
    # adjacent list
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            visited[curr_v] = True
            return 1 + dfs(curr_v)
        else:
            return 0

N, M = map(int, input().split())

# N : 정점의 개수
# M : 간선의 개수

graph = [[] for _ in range(N + 1)]

visited = [False for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, input().split())

    graph[start].append(end)
    graph[end].append(start)

print(dfs(1))