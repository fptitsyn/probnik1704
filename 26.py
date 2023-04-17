f = open("26.txt")
s, n = map(int, f.readline().split())
a = sorted([int(i) for i in f])
ans = []
for i in range(len(a)):
    if (sum(ans) + a[i]) <= s:
        ans.append(a[i])

print(len(ans))
mx = ans[-1]
print(mx)
# print(ans)
# print(s)
# print(sum(ans))
# for j in range(len(ans), len(a)):
#     if (sum(ans[::-1]) + a[j]) <= s:
#         ans.pop()
#         ans.append(a[j])
#         mx = max(mx, a[j])

