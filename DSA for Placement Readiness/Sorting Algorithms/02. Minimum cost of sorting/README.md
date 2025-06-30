<!-- problem:start -->

# Operation Difference

![Problem Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)
![Sorting](https://img.shields.io/badge/-Sorting-blue)

## Background

Bubble Sort is useful when the array is nearly sorted, as it can terminate early if no swaps occur during a pass. 
This is because if no swaps happen in a pass, it means that the array is already sorted. Breaking the loop early 
in such cases improves performance, preventing unnecessary iterations.

## Objectives

Given an array of integers along with the costs associated with comparison and swap operations, find the total cost incurred by Bubble Sort to sort the array in increasing order, ensuring that the algorithm terminates early when the array becomes sorted.

## Input Format

The input consists of three lines:
- The first line contains an integer **N** (`1 ≤ N ≤ 10⁵`), representing the number of elements in the array.
- The second line contains **N** space-separated integers, representing the elements of the array.
- The third line contains two space-separated integers, representing:
  - (`c_cmp`) → The cost of a single comparison operation.
  - (`c_swap`) → The cost of a single swap operation.
  
## Output Format

Print a single integer, representing the minimum total cost incurred to sort the array using Bubble Sort.

## Constraints

<ul>
    <li><code>1 ≤ N ≤ 10<sup>5</sup></code> (size of array)</li>
    <li><code>1 ≤ Costs ≤ 30</code></li>
</ul>

<!-- examples:start -->
## Sample Input
<pre>
<strong>6
4 2 5 3 7 9
2 3</strong>
</pre>

## Sample Output
<pre>
<strong>33</strong>
</pre>

## Explanation
The given array is 4 2 5 3 7 9, the cost of comparison is 2 and the cost of swapping is 3.

- On the first pass there are 5 comparisons and 2 swaps. The array is now 2 4 3 5 7 9.
- On the second pass there are 4 comparisons and 1 swap. The array is now 2 3 4 5 7 9.
- On the third pass there are 3 comparisons and no swaps. Since there are no swaps, the array is sorted and hence the loop breaks.

Total cost incurred = (5 + 4 + 3) * 2 + (2 + 1) * 3 = 24 + 9 = 33.
<!-- examples:end -->


## Solution

<!-- tabs:start -->

#### Python

```python
n = int(input())
arr = list(map(int, input().split()))
c_cmp, c_swap = map(int, input().split())


def bubble_sort(arr, c, s):
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


print(bubble_sort(arr, c_cmp, c_swap))
```
<!-- tabs:end -->
<!-- problem:end -->
