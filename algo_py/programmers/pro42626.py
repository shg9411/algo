import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while 1:
        if scoville[0]<K:
            if len(scoville)<2 or scoville[0]<=0:
                return -1
            tmp1 = heapq.heappop(scoville)
            tmp2 = heapq.heappop(scoville)
            heapq.heappush(scoville,tmp1+2*tmp2)
            answer+=1
        else:
            break
    return answer

scoville = [1,2,3,9,10,12]
k = 7
print(solution(scoville,k))