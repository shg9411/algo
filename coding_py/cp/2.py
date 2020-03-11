'''
arr에 담긴 물건들에 대해서
k개 이상을 선택하여
t원 이하의 가격을 만들 수 있는 경우의 수를 출력
'''
''' 2번째 방법
selected 배열을 없앰

def solution(arr, k, t):
    arr.sort()

    def dfs(idx, cnt, val):
        global res
        if val > t:
            return
        if cnt >= k:
            res += 1
        for i in range(idx, len(arr)):
            dfs(i+1, cnt+1, val+arr[i])

    dfs(0, 0, 0)
    return res
'''
answer = 0


def solution(arr, k, t):
    # 가격순으로 정렬
    arr.sort()
    selected = [False for _ in range(len(arr))]
    # 확인할 리스트
    res = []

    def select(idx):
        global answer
        # 가격이 t원 초과면 답이 될 수 없기에 return
        if sum(res) > t:
            return
        # 가격이 t원 이하이고 k개 이상 골랐기 때문에 정답이 될 수 있음
        # return을 하지 않는 이유는 더 담아도 가격이 t원 이하일 수 있기 때문
        if len(res) >= k:
            answer += 1
        for i in range(idx, len(arr)):
            # 물건 선택
            selected[i] = True
            res.append(arr[i])
            # 선택 후 재귀호출
            select(i+1)
            # 물건 선택 취소
            selected[i] = False
            # pop은 어차피 맨 뒤에 있는 원소를 제거하기 때문에 시간복잡도가 O(1)이라 ㄱㅊ
            res.pop()
    select(0)
    return answer


arr1 = [0, 0, 0, 0, 0]
k1 = 3
t1 = 10

print(solution(arr1, k1, t1))
