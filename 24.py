a = open("24.txt").readline()

# k = 0
# kmax = 0
# i = 0
# while i < len(a) - 2:
#     if a[i] in "CDF" and a[i + 1] in "CDF" and a[i + 2] in "AO":
#         k += 1
#         kmax = max(kmax, k)
#         i += 2
#     else:
#         k = 0
#     i += 1
#
# print(kmax)

a = a.replace("O", "A").replace("D", "C").replace("F", "C")
a = a.replace("CCA", "*")
a = a.replace("A", " ").replace("C", " ")
a = a.split()
print(len(max(a, key=len)))
