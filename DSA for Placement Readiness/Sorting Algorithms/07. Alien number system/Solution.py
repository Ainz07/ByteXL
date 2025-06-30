n = int(input())
arr = list(map(int, input().split()))
p = [0, 1, 9, 2, 8, 3, 7, 4, 6, 5]
print(*sorted(arr, key=lambda x: (len(str(x)), [p[int(d)] for d in str(x)])))