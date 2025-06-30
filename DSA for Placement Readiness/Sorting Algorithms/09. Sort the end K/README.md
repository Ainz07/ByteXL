<!-- problem:start -->

# Sort the end K

![Problem Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)
![Arrays](https://img.shields.io/badge/-Arrays-green)

## Background

You are working at a data analysis store, and often face unique challenges that require creative solutions. One such challenge recently came up when a client, a local retailer, needed to streamline their inventory tracking system. They wanted a way to sort the sales data only for their top-selling products while retaining the order of other product sales.

All the product sales numbers are unique. Can you leverage this fact to improve performance?
## Objectives

The goal is to create a program that uses a custom selection sort variant function to organize the top K elements of an array. This means sorting the highest K values to the end of the array while leaving the rest of the elements in their original order. This approach ensures that only the specified top elements are rearranged, maintaining the sequence of the remaining elements unchanged.
## Input Format

The input to your program consists of data to be sorted:
- The first line contains an integer **N**, the number of integers in the array.
- The second line contains **N** unique integers, representing the elements of the array.
- The third line contains an integer **K**, representing the number of top elements to be found and sorted.
  
## Output Format

Print **N** integers which is the array with top **K** elements sorted and placed on the right end and other elements in original order in the beginning.
## Constraints

<ul>
    <li><code>1 ≤ N ≤ 10<sup>5</sup></code> (size of array)</li>
    <li><code>0 ≤ K ≤ N</code>(number of top elements)</li>
</ul>

<!-- examples:start -->
## Sample Input
<pre>
<strong>4
3 28 1 4
2</strong>
</pre>

## Sample Output
<pre>
<strong>3 1 4 28</strong>
</pre>

## Explanation
The initial array is 3 28 1 4. You need to find and sort the top 2 values and place them in the end.
First find the top value which is 28 and place it at the end.
Then find the second-highest value which is 4 and place in 2nd last place.
Keep the rest of the elements in their original order in the beginning.

This gives you the array 3 1 4 28.
<!-- examples:end -->


## Solution

<!-- tabs:start -->

#### Python

```python
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

brr = []
for _ in range(k):
    x = max(arr)
    brr.append(x)
    arr.remove(x)

brr.reverse()
print(*arr, *brr)
```
<!-- tabs:end -->
<!-- problem:end -->
