f = open("27-A.txt")
n = f.readline()
sm = 0
min_desc = 100000000
b = []
for s in f:
    a = sorted([int(i) for i in s.split()], reverse=True)
    if (a[0] - a[1]) < min_desc:
        min_desc = a[0] - a[1]
        print(a)

    sm += a[1]
    b.append(a[1] % 2)
    print(a[1], a[1] % 2)

print(min_desc)
print(sm + min_desc)
print(b.count(1), b.count(0))
print(sm + min_desc)