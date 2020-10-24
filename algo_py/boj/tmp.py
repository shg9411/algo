N = int(input())
array = []
for i in range(N):
    num = int(input())
    array.append(num)
for i in range(0, N):
    min_value = 0
    for j in range(i, N):
        if min_value > array[j]:
            min_value = array[j]
    array[j] = array[i]
    array[i] = min_value
for i in array:
    print(i)