def solution(penter, pexit, pescape, data):
    answer = penter
    size = len(penter)
    i = 0
    packetLen = len(data)
    while i < packetLen:
        if data[i:i+size] in (penter, pexit, pescape):
            answer += pescape
        answer += data[i:i+size]
        i += size
    return answer+pexit
