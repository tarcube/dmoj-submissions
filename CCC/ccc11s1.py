# 100/100 AC 5pp
t = 0
s = 0
for i in range(int(input())):
    a = input()
    for j in range(len(a)):
        if a[j] == "t" or a[j] == "T":
            t += 1
        if a[j] == "s" or a[j] == "S":
            s += 1
if t > s:
    print("English")
else:
    print("French")