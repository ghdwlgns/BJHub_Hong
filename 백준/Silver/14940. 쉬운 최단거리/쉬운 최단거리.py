import sys
from collections import deque

n, m = map(int, input().split())

land_map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
distances = [[-1] * m for _ in range(n)]

for x in range(m):
    for y in range(n):
        if land_map[y][x] == 0:
            distances[y][x] += 1
        if land_map[y][x] == 2:
            start_x, start_y = x, y
            distances[y][x] = 0

def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        cx, cy = queue.popleft()

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < m and 0 <= ny < n and distances[ny][nx] == -1 and land_map[ny][nx] == 1:
                distances[ny][nx] = distances[cy][cx] + 1
                queue.append((nx, ny))

bfs(start_x, start_y)

for row in distances:
    print(" ".join(map(str, row)))
