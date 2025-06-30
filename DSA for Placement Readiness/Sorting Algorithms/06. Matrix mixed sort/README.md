<!-- problem:start -->

# Matrix mixed sort

![Problem Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)
![Sorting](https://img.shields.io/badge/-Sorting-blue)

## Background

You are working for a data analysis company and are generally required to sort data according to the needs. This time, you are given a matrix of integers which you need to sort in a given way that is: First each row and then sort each column of the matrix.

You are also instructed that for the given data, due to the way it is ordered, bubble sort would work well on sorting rows and selection sort would work well on sorting columns.
## Objectives

Your goal is to write a code to sort the matrix following the instructions given.


## Input Format

The input to your program consists of matrix to be sorted:
- The first line contains two integers, **N** and **M**, representing the number of rows and columns
- For each of the next **N** lines:
  - Each line contains **M** integers representing the values of the matrix.  
  
## Output Format

Print the matrix sorted after following the instructions.

## Constraints

<ul>
    <li><code>1 ≤ N ≤ 100</code> (number of rows)</li>
    <li><code>1 ≤ M ≤ 100</code> (number of columns)</li>
</ul>

<!-- examples:start -->
## Sample Input
<pre>
<strong>3 3
29 18 34
2 3 29
38 27 3</strong>
</pre>

## Sample Output
<pre>
<strong>2 3 29
3 27 34
18 29 38</strong>
</pre>

## Explanation
First sort the matrix rows using bubble sort which gives:

<pre>
<strong>18 29 34
2 3 29
3 27 38</strong>
</pre>

Then sort the columns using selection sort which gives:

<pre>
<strong>2 3 29
3 27 34
18 29 38</strong>
</pre>

<!-- examples:end -->


## Solution

<!-- tabs:start -->

#### Python

```python
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
```
<!-- tabs:end -->
<!-- problem:end -->
