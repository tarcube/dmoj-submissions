n = int(input())
arr = list(map(int, input().split()))
a = ""
for i in range(n):
    a += str(arr[i]) + " "
print(a[0:-1])
def bubblesort(n, arr):
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                a = ""
                for k in range(n):
                    a += str(arr[k]) + " "
                print(a[0:-1])
bubblesort(n, arr)