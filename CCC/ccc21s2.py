# 15/15 AC 7pp
a = int(input())
b = int(input())
c = int(input())
d = [0 for i in range(a)]
e = [0 for i in range(b)]
for i in range(c):
    f,g = map(str,input().split())
    if f == 'R':
        d[int(g)-1] += 1
    if f == 'C':
        e[int(g)-1] += 1
h = 0
for i in range(a):
    for j in range(b):
        if (d[i]+e[j]) % 2 == 1:
            h += 1
print(h)