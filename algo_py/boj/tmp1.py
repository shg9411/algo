'''
은행 창구 대기 시간이 언제 길어지는지 시뮬레이션 프로그램을 통해 알아보려 합니다. 시뮬레이션은 다음과 같은 방법으로 진행합니다.

창구 수를 설정합니다.
고객별로 대기 번호를 받은 시각과 상담에 걸리는 시간을 설정합니다.
생성된 데이터를 이용해 상담 처리 과정을 시뮬레이션합니다.
대기 번호를 받은 고객은 상담 창구가 비어있다면 대기 시간 없이 즉시 상담을 받습니다.
빈 창구가 없다면 빈 창구가 생길 때 까지 기다립니다.
상담 시간이 끝나면 고객은 돌아가고, 빈 창구가 하나 생깁니다.
단, 편의를 위해 시각은 0초부터 시작하며 모든 시간은 초 단위를 사용합니다. 또, 상담이 끝나 창구가 비면 즉시 다음 상담 업무를 처리합니다.

시뮬레이션 프로그램을 돌리던 중, 이번에는 전체 고객의 대기시간 합이 얼마인지 구해보려 합니다.
'''

import heapq


def solution(N, simulation_data):
    answer = 0
    size = len(simulation_data)
    i = 0
    t = 0
    q = []
    while i < size:
        if len(q) < N:
            heapq.heappush(q, simulation_data[i][0]+simulation_data[i][1])
        else:
            t = heapq.heappop(q)
            if t > simulation_data[i][0]:
                answer += t-simulation_data[i][0]
                heapq.heappush(q, t+simulation_data[i][1])
            else:
                heapq.heappush(q, simulation_data[i][0]+simulation_data[i][1])
        i += 1
    return answer


n = 1
simul = [[2, 3], [5, 4], [6, 3], [7, 4]]
print(solution(n, simul))
