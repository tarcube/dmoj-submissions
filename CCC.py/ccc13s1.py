# 150/150 AC 5pp
year = int(input())
running = True
while running:
    seen = []
    year += 1
    string = str(year)
    running = False
    for i in range(len(string)):
        if string[i] in seen:
            running = True
        else:
            seen.append(string[i])
print(year)