import sys

n, m = map(int, input().split())

graph = {i:[] for i in range(1, n + 1)}

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

is_visited = [False] * (n + 1)
result = 0

def dfs(node):
    stack = [node]

    while stack:
        cur = stack.pop()

        if not is_visited[cur]:
            is_visited[cur] = True
            stack.extend(graph[cur])

for i in range(1, n + 1):
    if not is_visited[i]:
        dfs(i)
        result += 1

print(result)
