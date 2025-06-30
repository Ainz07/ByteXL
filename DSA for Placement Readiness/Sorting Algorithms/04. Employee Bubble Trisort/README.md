<!-- problem:start -->

# Employee Bubble Trisort

![Problem Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)
![Sorting](https://img.shields.io/badge/-Sorting-blue)

## Background

In data management and analysis, sorting is a fundamental operation. When dealing with records that have multiple attributes, it is often necessary to apply multi-level sorting criteria. For example, in an employee database, we might want to sort employees primarily by age, then by salary if ages are the same, and by experience if both age and salary are the same. This ensures that the sorting is comprehensive and meets complex organizational needs.

For this question, you must not use any built-in sorting functions or libraries. Instead, your solution should involve developing a custom Bubble sort algorithm tailored to the specific sorting requirements outlined.

## Objectives

The objective of this task is to implement a custom Bubble sort algorithm that sorts records with three attributes: age, salary, and experience. The sorting should be performed in ascending order of age, then ascending order of salary for records with the same age, and finally in descending order of experience for records with the same age and salary.

## Input Format

The input to your program consists of data to be sorted:
- The first line contains an integer **N**, the number of records
- For each of the next **N** lines:
  - Each line contains three integers age, salary, and experience, separated by spaces representing a record.
  
## Output Format

Print **N** lines after sorting the records according to the conditions given in question.
## Constraints

<ul>
    <li><code>1 ≤ N ≤ 10<sup>5</sup></code> (number of records)</li>
    <li><code>1 ≤ Age, Experience ≤ 100</code> (Age, experience of employees)</li>
    <li><code>1 ≤ Salary ≤ 10<sup>5</sup></code> (Salary of employees)</li>
</ul>

<!-- examples:start -->
## Sample Input
<pre>
<strong>6
25 50000 3
25 50000 5
30 60000 2
25 40000 4
25 50000 2
30 60000 4</strong>
</pre>

## Sample Output
<pre>
<strong>25 40000 4
25 50000 5
25 50000 3
25 50000 2
30 60000 4
30 60000 2</strong>
</pre>

## Explanation
The sample output is obtained by sorting the employee records primarily by age in ascending order. Within each age group, records with the same age are sorted by salary in ascending order. Finally, if records have the same age and salary, they are sorted by experience in descending order.
<!-- examples:end -->
## Solution

<!-- tabs:start -->

#### Python

```python
arr = []
for _ in range(int(input())):
    age, slry, exp = map(int, input().split())
    arr.append([age, slry, exp])

for i in range(len(arr) - 1):
    for j in range(len(arr) - i - 1):
        if arr[j][0] > arr[j + 1][0]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

for i in range(len(arr) - 1):
    for j in range(len(arr) - i - 1):
        if arr[j][0] == arr[j + 1][0]:
            if arr[j][1] > arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

for i in range(len(arr) - 1):
    for j in range(len(arr) - i - 1):
        if arr[j][0] == arr[j + 1][0] and arr[j][1] == arr[j + 1][1]:
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

for x, y, z in arr:
    print(x, y, z)
```
<!-- tabs:end -->
<!-- problem:end -->
