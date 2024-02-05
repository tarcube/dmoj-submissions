n, x = map(int, input().split())
a = list(map(int, input().split()))
c = a.count(x)
if c > 0:
  print("YES")
else:
  hm = {}
  for i in range(n):
    for j in range(i+1, n):
      xor = a[i] ^ a[j]
      if xor in hm:
        hm[xor] += 1
      else:
        hm[xor] = 1
  if x in hm and hm[x] > 0:
    print("YES")
  else:
    print("NO")