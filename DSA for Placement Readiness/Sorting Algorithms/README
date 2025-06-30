# Operation Difference

**Max Score:** 5 | **Difficulty:** Hard

## Problem Description

You and your friend have recently learned about different sorting algorithms. You know that both Selection Sort and Bubble Sort have the same time complexity O(n²) but may perform differently based on the input. Your friend, however, believes that since their time complexities are the same, they will always perform equally well.

You decide to test this assumption by counting the total number of swaps required for both Bubble Sort and Selection Sort when sorting the same list.

## Background Information

While Selection Sort and Bubble Sort both have O(n²) time complexity, they differ in their approach:

- **Selection Sort**: Finds the minimum element in the unsorted portion and swaps it with the first element of the unsorted portion
- **Bubble Sort**: Repeatedly compares adjacent elements and swaps them if they're in the wrong order

Despite having the same time complexity, the number of swaps performed by each algorithm can vary significantly depending on the input array.

## Objective

Your task is to:
1. Implement both Bubble Sort and Selection Sort algorithms
2. Count the total number of swaps required to sort the list using each algorithm
3. Print the absolute difference between the number of swaps performed by the two sorting algorithms

## Input Format

The input consists of:
- **First line**: An integer `N` (1 ≤ N ≤ 10⁵), representing the number of elements in the array
- **Second line**: `N` space-separated integers, representing the elements of the array

## Output Format

Print a single integer representing the absolute difference between the number of swaps required by Bubble Sort and Selection Sort.

## Constraints

- 1 ≤ N ≤ 10⁴ (size of array)
- Array elements can be any integers

## Sample Input/Output

### Sample Input:
```
6
1 2 3 6 4 5
```

### Sample Output:
```
0
```

### Explanation:
It takes 2 swaps to sort the array using both bubble sort and selection sort, so the absolute difference is |2 - 2| = 0.

## Solution

```python
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
```

### Time and Space Complexity

- **Time Complexity**: O(n²) for both algorithms
- **Space Complexity**: O(1) auxiliary space for sorting, O(n) for array copies
