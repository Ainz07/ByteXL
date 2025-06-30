<!-- problem:start -->

# Alien number system

![Problem Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)
![Sorting](https://img.shields.io/badge/-Sorting-blue)

## Background

You've met an alien from another planet with a peculiar number system. Although they use base 10 like humans and the digits appear the same (0-9), each digit has a different value. After a confusing discussion, you both deduce that the alien's digits 0135798642 correspond to human digits 0123456789.

The alien wants to be sure if you understand its number system and hence it wants you to sort a list of numbers in non-descending order the way it would be sorted on his planet.
## Objectives

The objective is to implement a program using bubble sort to sort a list of numbers the way they would be sorted on the alien’s planet and print the numbers. You must implement the bubble sort function yourself and must not use any internal sorting libraries already available.


## Input Format

The input to your program consists of the numbers to be sorted:
- The first line contains an integer **N** representing the number of integers to be sorted. (N is in human number system)
- The second line contains an array of **N** space - separated integers.
  
## Output Format

Print an array of **N** integers which are sorted in non-descending order the way they would be on the alien’s planet.


## Constraints

<ul>
    <li><code>1 ≤ N ≤ 10<sup>3</sup></code></li>
</ul>

<!-- examples:start -->
## Sample Input
<pre>
<strong>5
1 9 2 4 5</strong>
</pre>

## Sample Output
<pre>
<strong>1 5 9 4 2</strong>
</pre>

## Explanation
To sort the numbers as per the alien system, we assign each number a value based on this alien digit mapping:
Number Alien Value (digit)
<pre>
<strong>1 → 1
9 → 5
2 → 9
4 → 8
5 → 3</strong>
</pre>

Now, sorting by alien value:
1 (1), 5 (3), 9 (5), 4 (8), 2 (9) → Sorted Output: 1 5 9 4 2
<!-- examples:end -->


## Solution

<!-- tabs:start -->

#### Python

```python
n = int(input())
arr = list(map(int, input().split()))
p = [0, 1, 9, 2, 8, 3, 7, 4, 6, 5]
print(*sorted(arr, key=lambda x: (len(str(x)), [p[int(d)] for d in str(x)])))
```
<!-- tabs:end -->
<!-- problem:end -->
