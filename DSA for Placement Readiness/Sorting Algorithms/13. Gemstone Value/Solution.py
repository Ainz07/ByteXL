n = int(input())
arr = sorted(map(int, input().split()))
ans = 0
for i in range(0, len(arr), 2):
    ans += arr[i]
print(ans)