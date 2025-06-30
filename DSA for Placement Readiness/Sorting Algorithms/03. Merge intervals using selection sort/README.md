<!-- problem:start -->

# Merge intervals using selection sort

![Problem Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)
![Sorting](https://img.shields.io/badge/-Sorting-blue)

## Background

Interval merging is a common problem encountered in computer science, often seen in scheduling, resource allocation, and other domains. Given a set of intervals, the task is to merge overlapping or adjacent intervals into a single interval. Implementing this efficiently is crucial for optimizing various algorithms and systems.

## Objectives

The objective of this task is to:

- Read interval data from input.
- Sort these intervals explicitly using Selection sort.
- Merge overlapping intervals.
- Output the merged intervals in a structured format.
- Note: You have to implement the sorting yourself and cannot use inbuilt sort functions.

## Input Format

- The first line contains an integer **N**, the number of intervals.
- The second line contains **N** integers representing start times of intervals.
- The third line contains **N** integers representing end times of intervals.
  
## Output Format

The program should produce output consisting of two lines:
- The first line should contain the merged start times, space-separated.
- The second line should contain the merged end times, space-separated.
## Constraints

<ul>
    <li><code>2 ≤ N ≤ 10<sup>5</sup></code> (number of intervals)</li>
</ul>

<!-- examples:start -->
## Sample Input
<pre>
<strong>4
1 2 8 15
3 6 10 18</strong>
</pre>

## Sample Output
<pre>
<strong>1 8 15
6 10 18</strong>
</pre>

## Explanation
The start times for intervals 1, 2, 3, 4 are 1, 2, 8, 15 respectively. 
The end times for intervals 1, 2, 3, 4 are 3, 6, 10, 18 respectively.
The start time for interval 2 is clashing with the end time of interval 1. Hence, they are merged.
The output is hence the start times of updated merged intervals on the first line and end times of the same on the next line.
<!-- examples:end -->


## Solution

<!-- tabs:start -->

#### Python

```python
def merge_intervals(intervals):
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    starts = [interval[0] for interval in merged]
    ends = [interval[1] for interval in merged]
    return starts, ends

n = int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
intervals = sorted([[arr[i], brr[i]] for i in range(n)])
starts, ends = merge_intervals(intervals)
print(' '.join(map(str, starts)))
print(' '.join(map(str, ends)))
```
<!-- tabs:end -->
<!-- problem:end -->
