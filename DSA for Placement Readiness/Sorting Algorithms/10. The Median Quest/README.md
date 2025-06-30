<!-- problem:start -->

# The Median Quest

![Problem Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)
![Sorting](https://img.shields.io/badge/-Sorting-blue)

## Problem Statement

Your task is to venture forth into the depths of Number-shire and uncover the secrets hidden within this array of integers. The array holds N integers, each possessing a unique essence and potential. However, only the median of these integers holds the true power to reveal the path forward.
The median of an array is the middle value when the array is sorted. If N is odd, it's simply the value at the position `(N+1)/2`. If N is even, it's the average of the values at positions i.e `(N/2)+((N/2)+1)`.
Once you have uncovered the median, your journey doesn't end there. Merlin has foreseen that the true guardians of the array's power are those numbers that surpass the might of the median. Your final task is to count how many integers in the array exceed this potent median value.

## Input Format

- The first line contains an integer **N** denoting the number of integers in the array.
- The second line contains **N** space-separated integers, each representing the mystical essence of a number.
  
## Output Format

Output a single integer, the count of integers in the array that hold power greater than the discovered median.

## Constraints

<ul>
    <li><code>1 ≤ N ≤ 100</code></li>
    <li><code>1 ≤ x ≤ 1000</code></li>
</ul>

<!-- examples:start -->
## Sample Input
<pre>
<strong>5
10 30 20 50 40</strong>
</pre>

## Sample Output
<pre>
<strong>2</strong>
</pre>

## Explanation
- Sorting the Array: Sort the array in ascending order: [10,20,30,40,50]
- Finding the Median: Since N (which is 5) is odd, the median is the middle element in the sorted array. The middle element in [10,20,30,40,50] is 30.
- Counting Numbers Greater than Median: Determine how many numbers in the array are greater than the median value (30). Numbers greater than 30 in the array are 40 and 50, which gives us a count of 2.
<!-- examples:end -->


## Solution

<!-- tabs:start -->

#### Python

```python
from statistics import median

n = int(input())
arr = sorted(map(int, input().split()))
print(sum(x > median(arr) for x in arr))
```
<!-- tabs:end -->
<!-- problem:end -->
