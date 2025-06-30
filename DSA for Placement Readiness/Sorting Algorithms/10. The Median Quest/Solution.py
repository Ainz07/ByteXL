from statistics import median

n = int(input())
arr = sorted(map(int, input().split()))
print(sum(x > median(arr) for x in arr))