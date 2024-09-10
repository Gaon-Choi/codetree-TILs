s, q = input().split()
q = int(q)

s = list(s)

for _ in range(q):
    mode, a, b = input().split()
    mode = int(mode)

    if mode == 1:
        a = int(a); b = int(b)
        s[a-1], s[b-1] = s[b-1], s[a-1]

        print(''.join(s))
    else:
        for i in range(len(s)):
            if s[i] == a:
                s[i] = b
        print(''.join(s))