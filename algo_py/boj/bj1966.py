def solution(location, priorities):
    answer = 0
    end = False
    while not end:
        for i, val in enumerate(priorities):
            mv = max(priorities)
            if val == mv:
                answer += 1
                if i == location:
                    end = True
                    break
                priorities[i] = 0
    return answer


if __name__ == '__main__':
    for _ in range(int(input())):
        print(solution(tuple(map(int, input().split()))[
            1], list(map(int, input().split()))))
