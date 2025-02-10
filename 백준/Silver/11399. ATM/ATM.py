import sys

n = int(input())
waiting_min_list = sorted(map(int, sys.stdin.readline().split()))

result = 0
cur = 0

for m in waiting_min_list:
    cur += m
    result += cur

print(result)
