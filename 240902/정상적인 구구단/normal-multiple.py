N = int(input())

for i in range(1, N+1):
    q = []
    for j in range(1, N+1):
        q.append("{i} * {j} = {m}".format(i=i,j=j,m=i*j))

    print(', '.join(q))