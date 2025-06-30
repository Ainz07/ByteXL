<!-- problem:start -->

# Maximize the Noise

![Problem Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)
![Sorting](https://img.shields.io/badge/-Sorting-blue)

## Background

In a futuristic town, drones equipped with powerful speakers patrol the streets to create noise that prevents unauthorized access to certain areas. These drones can generate noise by playing specific sequences of sounds, represented as strings consisting of the letters 's' and 'h'. The noise level is defined by how many times the subsequence "sh" appears in the sequence, where 's' comes before 'h'.
The drone currently has several preloaded sound sequences in its memory. You, as a security expert, need to maximize the noise produced by these sequences by arranging them in the optimal order before playing them.

## Objectives

Given a collection of strings in the drone's memory, reorder them to maximize the noise level of the combined sequence.
## Input Format

The input consists of three lines:
- The first line contains a single integer n (`1 ≤ N ≤ 10⁵`), the number of strings in the drone's memory.
- The next n lines contain the strings t1, t2, ..., tn, one per line. Each string consists of only the characters 's' and 'h', and the total length of all strings does not exceed 10⁵ characters.
  
## Output Format

Print a single integer — the maximum possible noise that can be achieved by optimally ordering the strings.

## Constraints

<ul>
    <li><code>1 ≤ N ≤ 10<sup>5</sup></code></li>
    <li><code>string = 's', 'h'</code></li>
</ul>

<!-- examples:start -->
## Sample Input
<pre>
<strong>4
ssh
hs
s
hhhs</strong>
</pre>

## Sample Output
<pre>
<strong>18</strong>
</pre>

## Explanation
In the first example, rearranging the strings to ssshhshhhs gives the maximum noise of 18.
<!-- examples:end -->


## Solution

<!-- tabs:start -->

#### Python

```python
n = int(input())
strings = [input().strip() for _ in range(n)]
data = [(s, s.count('s'), s.count('h')) for s in strings]
data.sort(key=lambda x: (x[1] / (x[2] + 1e-9)), reverse=True)
result = ''.join(d[0] for d in data)

s_count = 0
noise = 0
for c in result:
    if c == 's':
        s_count += 1
    else:
        noise += s_count

print(noise)
```
<!-- tabs:end -->
<!-- problem:end -->
