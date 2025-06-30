<!-- problem:start -->

# Selection Sentence Sort

![Problem Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)
![Sorting](https://img.shields.io/badge/-Sorting-blue)

## Background

Selection sort is a fundamental algorithm in computer science, known for its simplicity and straightforward implementation. It repeatedly steps through a list to find the smallest element and moves it to its correct position. This process is repeated for each element in the list until the entire list is sorted. The sorting algorithm can be adapted to meet specific ordering criteria beyond typical numerical or lexicographical sorting.

## Objectives

The objective is to sort a sentence such that capital letters appear first, followed by spaces, and finally lowercase letters, using the Selection sort algorithm. You must implement a custom Selection sort algorithm yourself and must not use any inbuilt sorting algorithms.
## Input Format

The input to your program consists of the string which is the sentence to be sorted. The first and only line of input is the sentence to be sorted.

## Constraints

<ul>
    <li><code>1 ≤ sentence length ≤ 10<sup>4</sup></code></li>
</ul>

<!-- examples:start -->
## Sample Input
<pre>
<strong>The Cat</strong>
</pre>

## Sample Output
<pre>
<strong>CT aeht</strong>
</pre>

## Explanation
The capital letters are sorted and placed in the beginning of the string and the small letters sorted are kept in the end.

<!-- examples:end -->


## Solution

<!-- tabs:start -->

#### Python

```python
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
```
<!-- tabs:end -->
<!-- problem:end -->
