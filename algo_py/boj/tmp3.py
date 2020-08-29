'''
문제 설명
n일 후 폐점하는 가게에서 상품 재고를 팔아 매출을 최대화하려 합니다. 각 상품들은 다음과 같이 판매됩니다.

모든 상품은 매일 정해진 수량만큼 팔립니다.
행사장에는 매대가 있는데 이 매대에서 파는 물건은 매일 정해진 수량의 2배만큼 팔립니다.
행사 매대에는 상품을 한 번에 한 종류만 올려놓고 팔 수 있습니다.
3-1. 매일 아침 한 번씩 그날 매대에 상품을 올릴지 말지, 올린다면 어떤 상품을 올릴지 정할 수 있습니다.
예를 들어 2일 후 폐점하는 가게에 상품이 다음과 같이 남았습니다.

재고량	개당 가격	일일 판매 수량
상품1	10	3	2
상품2	15	2	5
상품1을 이틀간 행사 매대에 올리면 상품1로 24원을, 상품2로 20원을 벌어 매출은 44원입니다.
상품2를 이틀간 행사 매대에 올리면 상품1로 12원을, 상품2로 30원을 벌어 매출은 42원입니다.
상품1과 상품2를 하루씩 행사 매대에 올리면 상품1로 18원을, 상품2로 30원을 벌어 매출은 48원입니다.
따라서 최대 매출은 48원입니다.

영업 일수 n, 상품의 정보를 담은 배열 products가 매개변수로 주어질 때, 가게가 n일 동안 영업 해 벌 수 있는 총 매출의 최댓값을 return 하도록 solution 함수를 작성해주세요.

제한사항
'''

import heapq


def solution(n, products):
    answer = 0
    q = []
    for product in products:
        answer += product[1]*min(product[0], product[2]*n)
        cnt = product[0]-product[2]*n
        if cnt > 0:
            heapq.heappush(q, [-min(cnt, product[2]) *
                               product[1], cnt, product[1], product[2]])
    if not q:
        return answer
    while n:
        money, cnt, price, can = heapq.heappop(q)
        money = -money
        answer += money
        cnt -= can
        if cnt > 0:
            heapq.heappush(q, [-min(cnt, can)*price, cnt, price, can])
        n -= 1
    return answer


n = 3
products = [[6, 5, 1], [11, 3, 2], [7, 10, 3]]
print(solution(n, products))
