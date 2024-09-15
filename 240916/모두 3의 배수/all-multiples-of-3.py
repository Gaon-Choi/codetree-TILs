is_all_triples = True


for _ in range(5):
    n = int(input())
    if n % 3 != 0:
        is_all_triples = False

if is_all_triples:
    print(1)
else:
    print(0)