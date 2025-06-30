arr = []
for _ in range(int(input())):
    age, slry, exp = map(int, input().split())
    arr.append([age, slry, exp])

for i in range(len(arr) - 1):
    for j in range(len(arr) - i - 1):
        if arr[j][0] > arr[j + 1][0]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

for i in range(len(arr) - 1):
    for j in range(len(arr) - i - 1):
        if arr[j][0] == arr[j + 1][0]:
            if arr[j][1] > arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

for i in range(len(arr) - 1):
    for j in range(len(arr) - i - 1):
        if arr[j][0] == arr[j + 1][0] and arr[j][1] == arr[j + 1][1]:
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

for x, y, z in arr:
    print(x, y, z)