def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)


def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if cmp(left[0], right[0]):
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result


def cmp(i,j):
    if pos[i] != pos[j]:
        return pos[i] < pos[j]
    i+=d
    j+=d
    if i<l and j<l:
        return pos[i] < pos[j]
    else:
        return i>j


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    pos_pivot = pos[pivot]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if pos[num] < pos_pivot:
            lesser_arr.append(num)
        elif pos[num] > pos_pivot:
            greater_arr.append(num)
        else:
            if num+d <l and pivot+d<l:
                if pos[num+d]<pos[pivot+d]:
                    lesser_arr.append(num)
                elif pos[num+d]>pos[pivot+d]:
                    greater_arr.append(num)
                else:
                    equal_arr.append(num)
            elif num+d > pivot+d :
                lesser_arr.append(num)
            elif pivot+d > num+d:
                greater_arr.append(num)
            else:
                equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

s = input()
l = len(s)
lcp = [0]*l
arr = [-1]*l
pos = [-1]*l
for i in range(l):
    arr[i] = i
    pos[i] = s[i]
d = 1
while 1:
    arr = quick_sort(arr)
    tmp = [0] * l
    for i in range(l-1):
        tmp[i+1] = tmp[i] + cmp(arr[i], arr[i+1])
    for i in range(l):
        pos[arr[i]] = tmp[i]
    if tmp[-1] == l-1:
        break
    d *= 2
k = 0
for i in range(l):
    k = max(k-1, 0)
    if pos[i] == l-1:
        continue
    j = arr[pos[i]+1]
    while i+k < l and j+k < l and s[i+k] == s[j+k]:
        k += 1
    lcp[pos[i]] = k
print(' '.join([str(i+1) for i in arr]))
print('x ',end='')
print(' '.join([str(v) for v in lcp[:-1]]))
