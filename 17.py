f = open("17.txt")

a = [int(i) for i in f]

ec = 0
es = 0
for i in a:
    if i % 2 == 0:
        ec += 1
        es += i

esr = es / ec

ans = []
for i in range(len(a) - 1):
    if (a[i] % 3 == 0 or a[i + 1] % 3 == 0) and (a[i] < esr or a[i + 1] < esr):
        ans.append(a[i] + a[i + 1])

print(len(ans), max(ans))