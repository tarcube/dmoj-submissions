# 20/100 TLE 1pp
n = int(input())
arr = list(map(int, input().split()))

def multiplyList(arr):
    result = 1
    for x in arr:
        result = result * x
    return result

def maxProduct(arr, k, n):
    window_product = multiplyList(arr[:k])
    l = 0
    r = k-1
    max_product = window_product
    for i in range(n - k):
        window_product = (window_product / arr[i]) * arr[i + k]
        if window_product > max_product:
            max_product = window_product
            l = i+1
            r = i+k
    return [max_product, l+1, r+1]

c = 0
d = []
for i in range(1,n+1):
    a = maxProduct(arr, i, n)
    b = a[0]/i
    if b > c:
        c = b
        d = [a[1], a[2]]
print(d[0], d[1])