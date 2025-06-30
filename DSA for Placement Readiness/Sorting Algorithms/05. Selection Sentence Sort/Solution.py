def selection_sort_custom(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if (arr[j].isupper() and not arr[min_idx].isupper()) or \
               (arr[j] == ' ' and arr[min_idx].islower()) or \
               (arr[j].isupper() and arr[min_idx].isupper() and arr[j] < arr[min_idx]) or \
               (arr[j] == ' ' and arr[min_idx] == ' ') or \
               (arr[j].islower() and arr[min_idx].islower() and arr[j] < arr[min_idx]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

s = input().strip()
sorted_chars = selection_sort_custom(list(s))
print("".join(sorted_chars), end="")