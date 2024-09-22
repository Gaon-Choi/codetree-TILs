n = int(input())

tree = [[] for _ in range(n)]

arr = list(map(int, input().split()))

rootNode = None

for i in range(len(arr)):
    if arr[i] == -1:
        rootNode = i
    else:
        tree[arr[i]].append(i)
        tree[i].append(arr[i])

# cut specific node
delete_node = int(input())

for node in tree:
    if node and delete_node in node:
        node.remove(delete_node)
    
tree.pop(delete_node)

total_leaf_number = 0

for node in tree:
    if len(node) == 0:
        total_leaf_number += 1

print(total_leaf_number - 1)