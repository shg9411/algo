import sys
import os
import heapq


def my_calc(file):
    def convert(i):
        return -int(i)
    f = open(file, "r")
    while True:
        try:
            n = int(f.readline())
            works = list(map(convert, f.readline().split(',')))
            heapq.heapify(works)
            for _ in range(n):
                heapq.heappush(works, min(heapq.heappop(works)+1, 0))
            answer = 0
            for work in works:
                answer += work**2
            print(answer)
        except:
            f.close()
            break


if __name__ == '__main__':
    file = sys.argv[1]
    my_calc(file)
