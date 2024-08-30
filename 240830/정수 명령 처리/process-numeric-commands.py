class Stack:
    def __init__(self):
        self.stack = []

    def push(self, elem):
        self.stack.append(elem)

    def empty(self):
        if not self.stack:
            return 1
        else:
            return 0

    def size(self):
        return len(self.stack)

    def top(self):
        return self.stack[self.size() - 1]

    def pop(self):
        return self.stack.pop()

N = int(input())

stack = Stack()

queries = []

for _ in range(N):
    text = input().split()
    queries.append(text)

for query in queries:
    if query[0] == "push":
        stack.push(int(query[1]))
    elif query[0] == "size":
        print(stack.size())
    elif query[0] == "empty":
        print(stack.empty())
    elif query[0] == "top":
        print(stack.top())
    elif query[0] == "pop":
        print(stack.pop())