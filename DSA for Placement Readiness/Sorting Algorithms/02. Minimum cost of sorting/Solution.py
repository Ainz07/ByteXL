n = int(input())
arr = list(map(int, input().split()))
c, s = map(int, input().split())

def bsort(arr, c, s):
    cost = 0
    n = len(arr)
    swapped = True
    pass_num = 0

    while swapped:
        swapped = False
        comparisons = 0
        swaps = 0

        for i in range(n - 1 - pass_num):
            comparisons += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
                swapped = True

        cost += comparisons * c + swaps * s
        pass_num += 1

    return cost

print(bsort(arr, c, s))