import sys

n = int(input())

point_list = [(x, y) for x, y in (map(int, sys.stdin.readline().strip().split()) for _ in range(n))]
point_list.sort(key=lambda x: (x[0], x[1]))

print('\n'.join(f'{x} {y}' for (x, y) in point_list))
