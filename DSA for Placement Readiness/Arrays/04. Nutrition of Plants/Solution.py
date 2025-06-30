n, m = map(int, input().split())
arr = list(map(int, input().split()))
brr = [0] * m

for _ in range(n):
    crr = list(map(int, input().split()))
    for i in range(m):
        brr[i] += crr[i]

for i in range(m):
    if brr[i] < arr[i]:
        print("No")
        break
else:
    print("Yes")