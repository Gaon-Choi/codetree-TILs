query = input()

brace_stack = []

for q in query:
    if q == "(":
        brace_stack.append('(')
    else:
        if len(brace_stack) == 0:
            print("No")
            exit(0)
        if brace_stack[-1] == ")":
            brace_stack.pop()
        else:
            print("No")
            exit(0)

print("Yes")