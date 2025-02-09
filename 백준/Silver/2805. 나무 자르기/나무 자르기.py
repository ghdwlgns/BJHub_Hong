import sys

n, m = map(int, input().split())

trees = [int(c) for c in sys.stdin.readline().split()]

start, end = 1, max(trees)
result = 0

while start <= end:
    mid = (start + end) // 2

    h = sum((cut := t - mid) if t - mid > 0 else 0 for t in trees)
    
    if h >= m:
        result = max(mid, result)
        start = mid + 1
    else:
        end = mid - 1

print(result)