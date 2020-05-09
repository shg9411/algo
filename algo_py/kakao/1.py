def solution(numbers, hand):
    answer = ''
    left = [1, 4, 7]
    right = [3, 6, 9]
    a = [[2], [1, 3, 5], [4, 6, 8], [7, 9, 0], ['*', '#']]
    b = [[5], [2, 4, 6, 8], [1, 3, 7, 9, 0], ['*', '#']]
    c = [[8], [5, 7, 9, 0], [2, 4, 6, '*', '#'], [1, 3]]
    d = [[0], [8, '*', '#'], [5, 7, 9], [2, 4, 6], [1, 3]]
    beforeL = '*'
    beforeR = '#'
    for num in numbers:
        if num in left:
            answer += 'L'
            beforeL = num
        elif num in right:
            answer += 'R'
            beforeR = num
        else:
            if num == 2:
                for idx, tmp in enumerate(a):
                    if beforeL in tmp:
                        ldist = idx+1
                    if beforeR in tmp:
                        rdist = idx+1
            elif num == 5:
                for idx, tmp in enumerate(b):
                    if beforeL in tmp:
                        ldist = idx+1
                    if beforeR in tmp:
                        rdist = idx+1
            elif num == 8:
                for idx, tmp in enumerate(c):
                    if beforeL in tmp:
                        ldist = idx+1
                    if beforeR in tmp:
                        rdist = idx+1
            else:
                for idx, tmp in enumerate(d):
                    if beforeL in tmp:
                        ldist = idx+1
                    if beforeR in tmp:
                        rdist = idx+1
            if ldist < rdist:
                beforeL = num
                answer += 'L'
            elif ldist > rdist:
                beforeR = num
                answer += 'R'
            else:
                if hand == 'right':
                    beforeR = num
                    answer += 'R'
                else:
                    beforeL = num
                    answer += 'L'
    return answer


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = 'right'

print(solution(numbers, hand))
