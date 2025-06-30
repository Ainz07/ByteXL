<!-- problem:start -->

# Operation Difference

[![Problem Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)](https://leetcode.com/tag/sorting)
[![Sorting](https://img.shields.io/badge/-Sorting-blue)](https://leetcode.com/tag/sorting)

## Background

You and your friend have recently learned about different sorting algorithms. You know that both Selection Sort and Bubble Sort have the same time complexity O(n²) but may perform differently based on the input.

Your friend, however, believes that since their time complexities are the same, they will always perform equally well.

You decide to test this assumption by counting the total number of swaps required for both Bubble Sort and Selection Sort when sorting the same list.

## Objective

Your task is to:
1. Implement both **Bubble Sort** and **Selection Sort**.
2. Count the total number of swaps required to sort the list using each algorithm.
3. Print the absolute difference between the number of swaps performed by the two sorting algorithms.

## Input Format

The input consists of:
- The first line contains an integer **N** (`1 ≤ N ≤ 10⁵`), representing the number of elements in the array.
- The second line contains **N** space-separated integers, representing the elements of the array.

## Output Format

Print a single integer representing the absolute difference between the number of swaps required by Bubble Sort and Selection Sort.


## Constraints

<ul>
    <li><code>1 ≤ N ≤ 10<sup>5</sup></code> (size of array)</li>
</ul>

<!-- examples:start -->
## Sample Input
<pre>
<strong>6
1 2 3 6 4 5</strong>
</pre>

## Sample Output
<pre>
<strong>0</strong>
</pre>

## Explanation
It takes 2 swaps to sort the array using both bubble sort and selection sort, so the absolute difference is |2 - 2| = 0.
<!-- examples:end -->


## Code Implementation

<!-- tabs:start -->

#### Python
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

print(abs(bubble_sort(arr2) - selection_sort(arr1)))
```
<!-- tabs:end -->
<!-- problem:end -->
