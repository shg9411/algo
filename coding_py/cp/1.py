def solution(goods, coupons):
    answer = 0
    # 높은 가격의 상품들에 대해 높은 할인율을 적용하는 것이 바른 선택
    # -> 상품과 쿠폰들을 내림차순으로 정렬
    goods.sort(reverse=True)
    coupons.sort(reverse=True)
    g_l = []
    c_l = []
    # 상품과 쿠폰들을 그대로 리스트에 담음
    for i, j in goods:
        g_l.extend([i for _ in range(j)])
    for i, j in coupons:
        c_l.extend([i for _ in range(j)])

    # 상품 리스트만큼 for문을 실행
    for i in range(len(g_l)):
        # try,except로 쿠폰이 남아있으면 할인을 적용하고
        try:
            answer += g_l[i]*(100-c_l[i])/100
        # 쿠폰이 남아있지 않으면 그 가격 그대로 적용
        except:
            answer += g_l[i]
    return answer


# 상품 가격들과 수량이 담긴 배열 goods
goods = [[25400, 2], [10000, 1], [31600, 1]]
# 쿠폰 할인율과 수량이 담긴 배열 coupons
coupons = [[5, 3], [23, 2], [11, 2], [9, 5]]
print(solution(goods, coupons))
