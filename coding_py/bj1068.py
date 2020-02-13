import sys
input = sys.stdin.readline

n = int(input())

node = [[] for _ in range(n+1)]

info = list(map(int, input().split()))
# 노드 인덱스에 자식 노드 저장
for idx, parent in enumerate(info):
    node[parent+1].append(idx)


# 자식이 없는 노드의 경우 -1로 사라진 노드로 표현 후 return, 아니라면 재귀형식으로 자식들을 자름
def cutChildren(n):
    if node[n+1] == []:
        node[n+1] = [-1]
        return
    for c in node[n+1]:
        cutChildren(c)
    # 사라진 노드는 -1로 표현
    node[n+1] = [-1]


# print(node) # 잘리기 전 노드의 모습
cut = int(input())
# 자르려는 노드가 부모노드인 경우 0을 출력,종료
if cut == node[0]:
    print(0)
    exit()
# 처음 입력 받았을 때 부모노드에서 자식을 제거
for n in node:
    if cut in n:
        n.remove(cut)
# 자식 제거 함수 호출
cutChildren(cut)
# print(node) #자르고 난 후 노드의 모습
count = 0
# 단말노드의 개수 카운트
for n in node[1:]:
    if n == []:
        count += 1
print(count)
