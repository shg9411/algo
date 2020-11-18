n = int(input())
cnt = [0]*(n+1)
for i in range(1, n+1):
    if i < 2:
        cnt[i] = cnt[i-1]+1
    elif i < 5:
        cnt[i] = min(cnt[i-1], cnt[i-2])+1
    elif i < 7:
        cnt[i] = min(cnt[i-1], cnt[i-2], cnt[i-5])+1
    else:
        cnt[i] = min(cnt[i-1], cnt[i-2], cnt[i-5], cnt[i-7])+1
print(cnt[n])
