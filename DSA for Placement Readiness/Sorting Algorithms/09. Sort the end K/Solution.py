n = int(input())
arr = list(map(int, input().split()))
k = int(input())

brr = []
for _ in range(k):
    x = max(arr)
    brr.append(x)
    arr.remove(x)

brr.reverse()
print(*arr, *brr)