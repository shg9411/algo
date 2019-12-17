s = input()
suffix = sorted([s[i:] for i in range(0,len(s))])
print('\n'.join(suffix))