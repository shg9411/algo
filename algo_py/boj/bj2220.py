n = int(input())

heap = [0, 1]

for i in range(2, n+1):
    heap.append(i)
    heap[i], heap[i-1] = heap[i-1], heap[i]
    j = i-1
    while j!=1:
        heap[j],heap[j//2] = heap[j//2],heap[j]
        j = j//2

print(*heap[1:])