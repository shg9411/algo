d, p, q = map(int, input().split())
if 0 in (d % p, d % q, d % (p+q)):
    print(d)
    exit()
if p < q:
    p, q = q, p
r = 2e9
for i in range(min(q, d//p+2)):
    tq = (d-p*i)//q
    for j in range(max(0, tq-2), tq+2):
        if (tr := p*i+q*j) < d:
            continue
        r = min(r, tr)
print(r)
