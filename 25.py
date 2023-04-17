k = 0
for i in range(500_000, 10_000_000):
    a = 0
    for j in range(9, int(i ** 0.5) + 1):
        if i % j == 0:
            if str(j).endswith("8"):
                a = j
                k += 1
                print(i, a)
                break
    if k == 5:
        break
