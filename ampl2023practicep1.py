n = int(input())
a = list(map(int, input().split()))
total = sum(a)
rem = total % 998244353
print(rem)