import heapq

class PriorityQueue:
    def __init__(self):
        self.items = []

    def push(self, item):
        heapq.heappush(self.items, item)

    def empty(self):
        return not self.items

    def size(self):
        return len(self.items)

    def pop(self):
        if self.empty():
            raise Exception("PriorityQueue is empty")
        return -heapq.heappop(self.items)
    
    def top(self):
        if self.empty():
            raise Exception("PriorityQueue is empty")
        return -self.items[0]

heap = PriorityQueue()


n = int(input())

for _ in range(n):
    query = input().split()

    if query[0] == "push":
        heap.push(int(query[1]))
    elif query[0] == "top":
        print(heap.top())
    elif query[0] == "size":
        print(heap.size())
    elif query[0] == "pop":
        print(-heap.pop())
    elif query[0] == "empty":
        if heap.empty():
            print(1)
        else:
            print(0)