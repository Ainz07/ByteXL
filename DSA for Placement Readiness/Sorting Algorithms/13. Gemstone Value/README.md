<!-- problem:start -->

# Gemstone Value

![Problem Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)
![Sorting](https://img.shields.io/badge/-Sorting-blue)

## Background

A unique board with 2n gemstones is used for a unique solo game. Each gemstone holds a positive integer value, and the player seeks to maximize their unique power by strategically pairing these gemstones.

## Objectives

You start with a unique power score of 0. Your goal is to perform n moves to maximize this score. Each move involves:
Selecting two gemstones with values x and y from the board.
Adding the lesser value, min(x,y), to your score.
Removing both gemstones from the board.
After n moves, all gemstones will be removed from the board. Your task is to determine the maximum unique power score achievable by optimally performing these moves.
## Input Format

- The first line contains an integer **n** `(1 ≤ n ≤ 50)` — representing half the number of gemstones.
- The second line contains **2n** integers a1, a2, …, a2n `(1≤ ai ≤ 10^7)` — the values of the gemstones.
  
## Output Format

Output a single integer — the maximum unique power score achievable.

## Constraints

<ul>
    <li><code>1 ≤ N ≤ 50</code></li>
    <li><code>1 ≤ ai ≤ 10<sup>7</sup></code></li>
</ul>

<!-- examples:start -->
## Sample Input
<pre>
<strong>2
1 3 5 2</strong>
</pre>

## Sample Output
<pre>
<strong>4</strong>
</pre>

## Explanation
The optimal pairs are (1, 2) and (3, 5). The score is 1 + 3 = 4.
<!-- examples:end -->


## Solution

<!-- tabs:start -->

#### Python

```python
n = int(input())
arr = sorted(map(int, input().split()))
ans = 0
for i in range(0, len(arr), 2):
    ans += arr[i]
print(ans)
```
<!-- tabs:end -->
<!-- problem:end -->
