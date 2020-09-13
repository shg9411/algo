n, m, q = map(int, input().split())
alpha = 'aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz'[:n*2]
print((alpha*(m//n+1))[:m])
