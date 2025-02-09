import sys

n, m = map(int, input().split())

trees = [int(c) for c in sys.stdin.readline().split()]

start, end = 1, max(trees)
result = 0

while start <= end:
    mid = (start + end) // 2

    h = sum(max(0, t - mid) for t in trees)
    
    if h >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
