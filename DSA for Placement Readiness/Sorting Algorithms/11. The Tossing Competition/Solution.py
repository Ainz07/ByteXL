arr = []

for _ in range(int(input())):
    a, b = map(int, input().split())
    arr.append(a / (a + b))

brr = []
for idx, val in enumerate(arr):
    brr.append((val, idx + 1))

brr.sort(key=lambda x: x[0], reverse=True)

for _, b in brr:
    print(b, end=' ')