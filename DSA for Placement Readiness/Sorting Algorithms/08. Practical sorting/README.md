<!-- problem:start -->

# Practical sorting


![Problem Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)
![Sorting](https://img.shields.io/badge/-Sorting-blue)

## Background

In real-world applications, sometimes sorting a list completely might not be necessary. For example, if the list is already partially sorted or if the requirement is to only move elements that differ significantly from their neighboring elements, a custom sorting approach can be more efficient. This can improve performance by achieving better speeds.

This can also be particularly useful in applications where preserving the relative order of elements is crucial unless they significantly deviate from each other.
## Objectives

Given an array and a permissible error value E, create a bubble sort function to sort the array in ascending order that only swaps elements differing by more than E. This preserves the relative order of elements with smaller differences and moves significantly different values to the correct positions. The final array should maintain elements with smaller differences in order.


## Input Format

The input to your program consists of array to be sorted and the threshold:
- The first line contains an integer **N**, the number of integers in the array.
- The second line contains **N** integers, representing the array elements.
- The third line contains an integer **E**, the threshold permissible error.
  
## Output Format

Output N integers which is the array sorted with relative order of elements with difference lesser than e is preserved.

## Constraints

<ul>
    <li><code>1 ≤ N ≤ 10<sup>5</sup></code> (size of array)</li>
    <li><code>0 ≤ E ≤ 10<sup>3</sup></code> (threshold)</li>
</ul>

<!-- examples:start -->
## Sample Input
<pre>
<strong>4
7 6 2 1
2</strong>
</pre>

## Sample Output
<pre>
<strong>2 1 7 6</strong>
</pre>

## Explanation
The array to be sorted is 7 6 2 1. Here, (7, 6) and (2, 1) have a difference smaller than the given threshold permissible error 2. Hence, their order is preserved and the final sorted array is 2 1 7 6.
It can be seen that in the final array, any two elements that are not in ascending order will have a difference smaller than or equal to the threshold value.
<!-- examples:end -->


## Solution

<!-- tabs:start -->

#### Python

```python
n = int(input())
arr = list(map(int, input().split()))
e = int(input())

for i in range(n - 1):
    for j in range(n - i - 1):
        if abs(arr[j] - arr[j + 1]) > e:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(*arr)
```
<!-- tabs:end -->
<!-- problem:end -->
