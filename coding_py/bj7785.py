import sys
input = sys.stdin.readline

n = int(input())

inCompany = set()

for _ in range(n):
    person, what = input().split()
    if what[0] == 'e':
        inCompany.add(person)
    else:
        inCompany.remove(person)
print('\n'.join(sorted(list(inCompany), reverse=True)))
