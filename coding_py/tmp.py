import sys
user_input = sys.stdin.readline().rstrip().upper()  # 올림으로 받는다
mystr = []

for i in range(len(user_input)):
    mystr.append(user_input[i])

# 글씨하나가 나올떄마다 카운트를 올린다
answer_list = {}
for i in mystr:
    count = answer_list.get(i, 0)
    answer_list[i] = count + 1

check = sorted(answer_list.values())
if check[-1] == check[-2]:
    print("?")
else:
    print(max(answer_list, key=(lambda k: answer_list[k])))
