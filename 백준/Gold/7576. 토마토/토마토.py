import sys
from collections import deque

m, n = map(int, input().split())

box_state = [[int(c) for c in sys.stdin.readline().split()] for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    queue = deque()
    
    queue.extend((x, y) for y in range(n) for x in range(m) if box_state[y][x] == 1)

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and box_state[ny][nx] == 0:
                box_state[ny][nx] = 1 + box_state[y][x]
                queue.append((nx, ny))

result = 0

bfs()

if any(0 in row for row in box_state):
    print(-1)
else:
    print(max(map(max, box_state)) - 1)
