s = ''.join(c*(c > '9') for c in input())
print(+(input() in s))
