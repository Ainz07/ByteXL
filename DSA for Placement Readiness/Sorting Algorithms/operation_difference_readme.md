# Operation Difference

**Max Score:** 5 | **Difficulty:** Hard

## Problem Description

You and your friend have recently learned about different sorting algorithms. You know that both Selection Sort and Bubble Sort have the same time complexity O(n²) but may perform differently based on the input. Your friend, however, believes that since their time complexities are the same, they will always perform equally well.

You decide to test this assumption by counting the total number of swaps required for both Bubble Sort and Selection Sort when sorting the same list.

## Background Information

While Selection Sort and Bubble Sort both have O(n²) time complexity, they differ in their approach:

- **Selection Sort**: Finds the minimum element in the unsorted portion and swaps it with the first element of the unsorted portion
- **Bubble Sort**: Repeatedly compares adjacent elements and swaps them if they're in the wrong order

Despite having the same time complexity, the number of swaps performed by each algorithm can vary significantly depending on the input array.

## Objective

Your task is to:
1. Implement both Bubble Sort and Selection Sort algorithms
2. Count the total number of swaps required to sort the list using each algorithm
3. Print the absolute difference between the number of swaps performed by the two sorting algorithms

## Input Format

The input consists of:
- **First line**: An integer `N` (1 ≤ N ≤ 10⁵), representing the number of elements in the array
- **Second line**: `N` space-separated integers, representing the elements of the array

## Output Format

Print a single integer representing the absolute difference between the number of swaps required by Bubble Sort and Selection Sort.

## Constraints

- 1 ≤ N ≤ 10⁴ (size of array)
- Array elements can be any integers

## Sample Input/Output

### Sample Input:
```
6
1 2 3 6 4 5
```

### Sample Output:
```
0
```

### Explanation:
It takes 2 swaps to sort the array using both bubble sort and selection sort, so the absolute difference is |2 - 2| = 0.

## Solution

```python
# Read input
n = int(input())
arr = list(map(int, input().split()))

def selection_sort(arr):
    """
    Implementation of Selection Sort algorithm
    Returns the number of swaps performed
    """
    swaps = 0
    for i in range(n - 1):
        min_idx = i
        # Find the minimum element in the remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    
    return swaps

def bubble_sort(arr):
    """
    Implementation of Bubble Sort algorithm
    Returns the number of swaps performed
    """
    swaps = 0
    for i in range(n):
        # Last i elements are already in place
        for j in range(n - 1 - i):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    
    return swaps

# Create copies of the original array for each sorting algorithm
arr1 = arr.copy()
arr2 = arr.copy()

# Apply sorting algorithms and count swaps
a = selection_sort(arr1)
b = bubble_sort(arr2)

# Print the absolute difference between swap counts
print(abs(b - a))
```

## Logic and Approach

### Algorithm Implementation Strategy

1. **Input Processing**: 
   - Read the array size `n` and the array elements
   - Create separate copies of the array for each sorting algorithm to ensure fair comparison

2. **Selection Sort Logic**:
   - For each position `i` from 0 to n-2:
     - Find the minimum element in the subarray from index `i` to `n-1`
     - If the minimum element is not at position `i`, swap it with the element at position `i`
     - Increment swap counter only when an actual swap occurs
   - **Key Insight**: Selection sort performs at most n-1 swaps (one swap per position)

3. **Bubble Sort Logic**:
   - For each pass `i` from 0 to n-1:
     - Compare adjacent elements from index 0 to n-2-i
     - Swap adjacent elements if they are in wrong order (left > right)
     - Increment swap counter for each swap performed
   - **Key Insight**: Bubble sort can perform many more swaps as it only moves elements one position at a time

4. **Comparison and Output**:
   - Calculate the absolute difference between swap counts
   - The difference reveals how the algorithms perform differently on the same input

### Time and Space Complexity

- **Time Complexity**: O(n²) for both algorithms
- **Space Complexity**: O(1) auxiliary space for sorting, O(n) for array copies
- **Swap Complexity**: 
  - Selection Sort: O(n) swaps maximum
  - Bubble Sort: O(n²) swaps maximum

### Why Different Swap Counts?

- **Selection Sort**: Makes fewer swaps because it directly places each element in its final position
- **Bubble Sort**: May make more swaps because it only moves elements one position at a time through adjacent swaps
- The difference depends on the initial arrangement of elements in the array

### Edge Cases Handled

- Already sorted array: Both algorithms will perform minimal swaps
- Reverse sorted array: Maximum difference between swap counts
- Single element: No swaps needed for either algorithm
- Identical elements: Minimal swaps for both algorithms

This solution demonstrates that while two algorithms may have the same time complexity, their practical performance characteristics (like number of operations) can differ significantly based on the input data structure.