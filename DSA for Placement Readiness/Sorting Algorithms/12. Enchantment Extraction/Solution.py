import heapq

n = int(input())
arr = list(map(int, input().split()))
heapq.heapify(arr)
maxi = 0

while arr:
    x = heapq.heappop(arr)
    maxi = max(maxi, x)
    for i in range(len(arr)):
        arr[i] -= x
    heapq.heapify(arr)

print(maxi)