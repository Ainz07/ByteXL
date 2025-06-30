<!-- problem:start -->

# Enchantment Extraction

![Problem Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)
![Heaps](https://img.shields.io/badge/-Heaps-rebeccapurple)

## Objective

Elara can perform an operation called "enchantment extraction" on the array, which works as follows:
Find the crystal with the least enchantment level, denoted as m.
Remove this crystal from the array.
Subtract m from the enchantment level of each remaining crystal in the array.
Elara wants to know the maximum possible minimum enchantment level of the crystals after performing the "enchantment extraction" operation any number of times (including zero). [Minimum Merge : 32]
## Input Format

- The first line contains an integer **n** `(1 ≤ n ≤ 200,000)` — the number of enchanted crystals.
- The second line contains **n** space-separated integers **pi** `(−1,000,000,000 ≤ pi ≤ 1,000,000,000)` — the enchantment level of each crystal.
  
## Output Format

Print a single integer — the maximum possible minimum enchantment level of the crystals after performing the "enchantment extraction" operations.

## Constraints

<ul>
    <li><code>1 ≤ N ≤ 200,000</code></li>
    <li><code>−1,000,000,000≤ pi ≤ 1,000,000,000</code></li>
</ul>

<!-- examples:start -->
## Sample Input
<pre>
<strong>5
1 6 -4 -2 -4</strong>
</pre>

## Sample Output
<pre>
<strong>5</strong>
</pre>

## Explanation
The initial array is [1, 6, -4, -2, -4].
Perform "enchantment extraction" by removing -4 and adjusting the array: [1-(-4), 6-(-4), -2-(-4), -4-(-4)] = [5, 10, 2, 0].
Continue with further extractions if needed to maximize the minimum enchantment level.

Total cost incurred = (5 + 4 + 3) * 2 + (2 + 1) * 3 = 24 + 9 = 33.
<!-- examples:end -->


## Solution

<!-- tabs:start -->

#### Python

```python
import heapq

n = int(input())
arr = list(map(int, input().split()))
heapq.heapify(arr)
maxi = 0

while arr:
    x = heapq.heappop(arr)
    maxi = max(maxi, x)
    for i in range(len(arr)):
        arr[i] -= x
    heapq.heapify(arr)

print(maxi)
```
<!-- tabs:end -->
<!-- problem:end -->
