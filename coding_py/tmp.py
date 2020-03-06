# 틀린 코드
def Delete(num, graph):
    graph[num] = -1
    for i in range(len(graph)):
        if num == graph[i]:
            Delete(i, graph)


N = int(input())
graph = list(map(int, input().split()))
num = int(input())

Delete(num, graph)
count = 0
print(graph)
for i in range(len(graph)):
    if graph[i] != -1 and i not in graph:
        count += 1
print(count)

# 맞는 코드