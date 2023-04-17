def f(x, q):
    a = []
    while x > 0:
        a.append(x % q)
        x //= q
    return a[::-1]


d = 36**7 + 6**19 - 18
print(f(d, 6).count(5))