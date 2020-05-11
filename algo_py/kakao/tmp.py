
def solution(arr):
    answer = 1
    tmp = dict()
    arr.sort()
    for i in arr:
        cnt = 1
        while 1:
            if i in tmp:
                cnt += tmp[i].pop()
                if tmp[i] == []:
                    tmp.pop(i)
                i *= 2
            else:
                tmp[i] = [cnt]
                break
    answer = sorted(tmp.items(), key=lambda x: x[1])[-1][1]
    return answer


weights = [2,2,2,2,3,3,5,6]
print(solution(weights))
