def f(n):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        r = "10" + b[2:] + "0"
    else:
        r = "11" + b[2:] + "1"
    return int(r, 2)

ans = []
for n in range(1, 1000):
    r = f(n)
    if r > 40:
        ans.append(n)

print(min(ans))