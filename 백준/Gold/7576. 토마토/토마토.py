import sys
from collections import deque

m, n = map(int, input().split())

box_state = [[int(c) for c in sys.stdin.readline().split()] for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    queue = deque()
    for x in range(m):
        for y in range(n):
            if box_state[y][x] == 1:
                queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            if 0 <= x + dx < m and 0 <= y + dy < n and box_state[y + dy][x + dx] == 0:
                box_state[y + dy][x + dx] = 1 + box_state[y][x]
                queue.append((x + dx, y + dy))

all_ripe = True
result = 0

bfs()

for x in range(m):
    for y in range(n):
        if box_state[y][x] == 0:
            all_ripe = False
            break
        elif box_state != -1:
            result = max(result, box_state[y][x])

    if not all_ripe:
        break

if not all_ripe:
    print(-1)
else:
    print(result - 1)
    