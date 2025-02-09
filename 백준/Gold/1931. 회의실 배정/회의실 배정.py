import sys

n = int(input())

meetings = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
meetings.sort(key=lambda x: (x[1], x[0]))

result, last = 0, 0

for start, end in meetings:
    if start >= last:
        result += 1
        last = end

print(result)
