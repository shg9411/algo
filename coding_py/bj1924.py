x, y = map(int, input().split())

date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
s = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
day = y-1
month = x-1
for i in range(month):
    day += date[i]
print(s[day%7])