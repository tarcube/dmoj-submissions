# 50/50 AC 5pp
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = 1
f = 0
while a != 0:
    if e == 1:
        a -= 1
        f += 1
        b += 1
        if b == 35:
            b = 0
            a += 30
        e = 2
    elif e == 2:
        a -= 1
        f += 1
        c += 1
        if c == 100:
            c = 0
            a += 60
        e = 3
    elif e == 3:
        a -= 1
        f += 1
        d += 1
        if d == 10:
            d = 0
            a += 9
        e = 1
print("Martha plays "+str(f)+" times before going broke.")