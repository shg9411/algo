def partition(num, cnt):
    if cnt == 1:
        return [[num]]
    else:
        ret = []
        for i in range(1, num-cnt+2):
            for j in partition(num-i, cnt-1):
                temp = [i]+j
                ret.append(temp)
        return ret


def same_list(lst):
    ret = []
    size = len(lst)
    for start in range(size):
        temp = lst[start:size]
        temp += lst[:start]
        ret.append(temp)
    return ret


def calc_dis(lst, n):
    ret = []
    for cur in lst:
        temp = 0
        for i in range(len(cur)-1):
            if cur[i] > cur[i+1]:
                temp += n-cur[i]+cur[i+1]
            else:
                temp += cur[i+1]-cur[i]
        ret.append(temp)
    return ret


def solution(n, weak, dist):
    answer = 0
    dist = sorted(dist, reverse=True)

    for i in range(len(dist)):

        member = dist[:i+1]

        prev = partition(len(weak), i+1)
        part_list = []

        while len(prev) != 0:
            cur = prev.pop()
            lst = same_list(cur)
            for idx, val in enumerate(prev):
                if val in lst:
                    del(prev[idx])
            part_list.append(cur)

        for part in part_list:
            for idx in range(len(weak)):
                weak_partition = []
                cnt = 0
                for cur in part:
                    temp = []
                    for j in range(cur):
                        temp.append(weak[(idx+cnt) % len(weak)])
                        cnt += 1
                    weak_partition.append(temp)

                dis_list = sorted(calc_dis(weak_partition, n), reverse=True)
                flag = True
                for j in range(len(dis_list)):
                    if member[j] < dis_list[j]:
                        flag = False
                        break

                if flag:
                    return i+1
    return -1
