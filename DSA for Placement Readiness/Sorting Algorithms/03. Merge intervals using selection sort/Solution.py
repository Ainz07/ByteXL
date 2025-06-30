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