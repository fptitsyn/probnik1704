def f(s, c, m):
    if s >= 39:
        return c % 2 == m % 2
    if c > m:
        return 0
    a = [f(s + 1, c + 1, m), f(s * 3, c + 1, m)]
    if (c + 1) % 2 == m % 2:
        return any(a)
    else:
        return all(a)

for s in range(1, 39):
    for m in range(1, 7):
        if f(s, 0, m):
            print(s, m)
            break