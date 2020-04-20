# -*- coding:utf-8 -*-
from itertools import combinations
#import time

#이진법문자란 문자열 "acddc"에 있는 문자를 a를 이진법 1의 자리로 부터 변환한 것
#즉 "acddc"의 이진법문자는 0b1101(혹은 13)임. 물론 이것은 정수형 자료.

def WordtoNum(s): #입력된 문자열을 a,c,i,n,t 제외하고 이진법문자으로 변경
    result = 0
    s=list(set(s)-{"a","n","c","t","i"})
    for i in s:
        result |= 1 << (ord(i)-97)
    return result

def NumtoWord(a): #이진법문자로 표현된 것 중 1로 표현된 지수들을 집합으로 반환 
    result = set()
    i = 0
    while a:
        if a&1 == 1:
            result.add(i)
        a = a >> 1
        i += 1
    return result

def TuptoNum(s): #조합에서 선택된 튜블을 이진법문자로 표현
    result = 0
    for i in s:
        result |= 1 << i
    return result

n, k = map(int, input().split())
WordsLst=[]
WholeWords = 0
ans = 0

for _ in range(n):
    Word = input()[4:-4]
    Num = WordtoNum(Word)
    WordsLst.append(Num)
    WholeWords |= Num

#start = time.time()

NumSet = NumtoWord(WholeWords)

if len(NumSet) < k-5:
    k = len(NumSet) + 5
for spellin in combinations(NumSet, k-5):
    cnt = 0
    TempNum = TuptoNum(spellin)
    for i in WordsLst:
        if TempNum|i == TempNum:
            cnt += 1
    ans = max(ans,cnt)
    
print(ans)
#print("time :", time.time() - start)