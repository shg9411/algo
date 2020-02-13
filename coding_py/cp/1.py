def solution(goods,coupons):
    answer = 0
    goods.sort(reverse=True)
    coupons.sort(reverse=True)
    goods_list = []
    coupon_list = []
    for i,j in goods:
        for _ in range(j):
            goods_list.extend([i])
    for i,j in coupons:
        for _ in range(j):
            coupon_list.append(i)
    for i in range(len(goods_list)):
        answer+=goods_list[i]*(100-coupon_list[i])/100
    return answer    

goods = [[25400, 2], [10000, 1], [31600, 1]]
coupons = [[5, 3], [23, 2], [11, 2], [9, 5]]
print(solution(goods,coupons))