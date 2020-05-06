def solution(heights):
    answer = []
    for s_idx in range(len(heights)-1, -1, -1):
        flag = False
        for r_idx in range(s_idx-1, -1, -1):
            if heights[s_idx] < heights[r_idx]:
                flag = True
                answer = [r_idx + 1] + answer
                break
        if not flag:
            answer = [0] + answer
    return answer
