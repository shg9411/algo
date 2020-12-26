def solution(s1, s2):
    answer = s1+s2 if s1+s2 < s2+s1 else s2+s1
    if s1 == s2:
        return s1
    l1 = len(s1)
    l2 = len(s2)
    for i in range(l1):
        for j in range(l2):
            if s1[:i] == s2[j:]:
                tmp = s2+s1[i:]
                if len(tmp) < len(answer):
                    answer = tmp
                elif len(tmp) == len(answer) and tmp <= answer:
                    answer = tmp
            if s2[:j] == s1[i:]:
                tmp = s1+s2[j:]
                if len(tmp) < len(answer):
                    answer = tmp
                elif len(tmp) == len(answer) and tmp <= answer:
                    answer = tmp
    return answer


print(solution("ABC", "BCA"))
