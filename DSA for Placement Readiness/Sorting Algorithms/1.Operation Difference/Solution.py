n = int(input())
arr = list(map(int, input().split()))


def selection_sort(arr):
    swaps = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    return swaps


def bubble_sort(arr):
    swaps = 0
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return swaps


arr1 = arr.copy()
arr2 = arr.copy()

a = selection_sort(arr1)
b = bubble_sort(arr2)

print(abs(b - a))