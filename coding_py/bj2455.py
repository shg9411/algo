people = [0]*5
for i in range(1,5):
    down, up = map(int,input().split())
    people[i] = people[i-1] + up-down
print(max(people))