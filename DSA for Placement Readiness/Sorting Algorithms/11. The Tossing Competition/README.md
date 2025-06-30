<!-- problem:start -->

# The Tossing Competition

![Problem Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)
![Sorting](https://img.shields.io/badge/-Sorting-blue)

## Background

In a city, each citizen participates in an annual coin-tossing competition. Each citizen is numbered from 1 to N, and they keep a record of the number of heads and tails they get during their coin tosses. The goal is to rank the most successful citizens based on their coin toss success rates.

## Objective

Determine the ranking of the citizens based on their success rates in descending order. The success rate is defined as the ratio of heads to the total number of tosses. In case of ties, rank the citizens with the same success rate by their assigned numbers in ascending order.

## Input Format

- The first line contains an integer **n** `(1 ≤ n ≤ 10⁵)` — the number of citizens.
- The next n line contains two numbers **Ai**, **Bi**
  - **Ai** is the number of heads for citizen i.
  - **Bi** is the number of tails for citizen i.
  
## Output Format

Print the numbers of citizens 1, 2, ..., N in descending order of their success rates, with ties broken in ascending order of their assigned numbers.

## Constraints

<ul>
    <li><code>2 ≤ N ≤ 2x10<sup>5</sup></code></li>
    <li><code>0 ≤ Ai,Bi ≤ 10<sup>9</sup></code></li>
    <li><code> Ai + Bi ≥ 1</code></li>
</ul>

<!-- examples:start -->
## Sample Input
<pre>
<strong>3
3 1
2 2
1 3</strong>
</pre>

## Sample Output
<pre>
<strong>1 2 3</strong>
</pre>

## Explanation
Citizen 1 has a success rate of 3/4, Citizen 2 has a success rate of 2/4, and Citizen 3 has a success rate of 1/4. Therefore, they are ranked in that order.
<!-- examples:end -->


## Solution

<!-- tabs:start -->

#### Python

```python
arr = []

for _ in range(int(input())):
    a, b = map(int, input().split())
    arr.append(a / (a + b))

brr = []
for idx, val in enumerate(arr):
    brr.append((val, idx + 1))

brr.sort(key=lambda x: x[0], reverse=True)

for _, b in brr:
    print(b, end=' ')
```
<!-- tabs:end -->
<!-- problem:end -->
