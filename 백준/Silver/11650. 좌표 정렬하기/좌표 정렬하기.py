import sys

n = int(input())

point_list = [(x, y) for x, y in (map(int, sys.stdin.readline().split()) for _ in range(n))]
point_list.sort()

print('\n'.join(f'{x} {y}' for (x, y) in point_list))
