a, b = map(int, input().split())

print('''{a} * {b} = {mult}
{a} / {b} = {div}'''.format(a=a, b=b, mult=a*b, div=a//b))