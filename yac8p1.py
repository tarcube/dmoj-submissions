n = int(input())
l = list(map(int, input().split()))
# bubble sort
c = 0
for i in range(n):
  for j in range(n-1, i, -1):
    if l[j] < l[j-1]:
      l[j], l[j-1] = l[j-1], l[j]
      c += 1
print(c+1)