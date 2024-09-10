import sys
sys.setrecursionlimit(10**6)

START_POINT = None

def dfs(vertex, curr_distance = 0):

    farthest_node = vertex
    max_distance = curr_distance

    # adjacent list
    for v, cost in tree[vertex]:
        if not visited[v]:
            #parent[curr_v] = vertex
            visited[v] = True
            distance, node = dfs(v, curr_distance + cost)
            if distance > max_distance:
                max_distance = distance
                farthest_node = node
    
    return max_distance, farthest_node

n = int(input())

tree = [[] * (n + 1) for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(n-1):
    start, end, cost = map(int, input().split())
    if START_POINT is None:
        START_POINT = start
    tree[start].append((end, cost))
    tree[end].append((start, cost))

mx_dist, f_node = dfs(START_POINT, 0)

# 방문 정보 초기화
visited = [False] * (n + 1)

visited[f_node] = True
diameter, _ = dfs(f_node, 0)

print(diameter)