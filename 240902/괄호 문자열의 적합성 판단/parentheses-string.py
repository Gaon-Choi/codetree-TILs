query = input()

brace_stack = []

for q in query:
    if q == "(":
        brace_stack.append('(')
    else:
        if len(brace_stack) > 0 and brace_stack[-1] == "(":
            brace_stack.pop()
        else:
            print("No")
            exit(0)

if not brace_stack:
    print("Yes")
else:
    print("No")