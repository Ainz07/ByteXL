n = int(input())
arr = list(map(int, input().split()))
k = int(input())

found = False

i = 0
while (j := i + k) <= n:
    window = arr[i:j]
    if all(x % 2 == 0 for x in window):
        print(*window)
        found = True
    i += 1

if not found:
    print(-1)