a, b = map(int, input().split())
mat = []

for _ in range(a):
    row = list(map(int, input().split()))
    mat.append(row)

def bubble_sort(arr):
    for i in range(a):
        for j in range(a - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(mat, col):
    cols = [m[col] for m in mat]
    for i in range(a - 1):
        mini = i
        for j in range(i + 1, a):
            if cols[j] < cols[mini]:
                mini = j
        cols[i], cols[mini] = cols[mini], cols[i]

    for i in range(a):
        mat[i][col] = cols[i]

for row in mat:
    bubble_sort(row)

for col in range(b):
    selection_sort(mat, col)

for m in mat:
    print(*m)