query = input()

brace_stack = []

for q in query:
    if q == "(":
        brace_stack.append('(')
    else:
        if brace_stack[-1] == ")":
            brace_stack.pop()

if not brace_stack:
    print("Yes")
else:
    print("No")