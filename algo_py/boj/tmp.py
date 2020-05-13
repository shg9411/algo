a = input()
aa = a.upper()  # 대문자로 만듦
aa = list(aa)
aa.sort()  # 알파벳순
li = []
l = []

pp = list(set(aa))  # 1.pp를 새로 선언해 중복값 제거


for j in range(len(aa)):
    qw = aa.count(aa[j])  # 알파벳 개수 구함

    l.append(qw)

mmm = max(l)
ind = l.index(mmm)

yy = list(set(l))  # 2.yy 선언해 중복값제거


hh = l.count(mmm)

if mmm < hh:
    print("?")
else:
    print(aa[ind])
