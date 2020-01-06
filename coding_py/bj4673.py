natural_number_set = set(range(1, 10001))
generated_number_set= set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generated_number_set.add(i)

self_number_set = natural_number_set - generated_number_set

for i in sorted(self_number_set):
    print(i)