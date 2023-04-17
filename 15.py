ans = []
for a in range(500):
    for x in range(500):
        for y in range(500):
            if not ((x * y < 100) or (y >= a) or (x > a)):
                break
        if not ((x * y < 100) or (y >= a) or (x > a)):
            break
    else:
        ans.append(a)

print(max(ans))