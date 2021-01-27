from collections import Counter


def solution(card, word):
    line = []
    for c in card:
        line.append(Counter(c))
    answer = []
    for w in word:
        check = [1, 1, 1]
        tmp = Counter(w)
        for key, value in tmp.items():
            can = False
            for idx, l in enumerate(line):
                if l.get(key, 0) >= value:
                    check[idx] = 0
                    can = True
                    break
            if not can:
                break
        if not can or any(check):
            continue
        else:
            answer.append(w)

    return answer if answer else ["-1"]


card = ["ABACDEFG", "NOPQRSTU", "HIJKLKMM"]
word = ["GPQM", "GPMZ", "EFU", "MMNA"]
print(solution(card, word))