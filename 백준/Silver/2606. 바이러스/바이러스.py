import sys

n = int(input())

computer_graph = {i: [] for i in range(1, n + 1)}
is_visited = [False] * (n + 1)

for _ in range(int(input())):
    start, end = map(int, sys.stdin.readline().split())
    computer_graph[start].append(end)
    computer_graph[end].append(start)

result = 0

def dfs():
    stack = [1]
    result = 0

    while stack:
        cur = stack.pop()
        if not is_visited[cur]:
            stack.extend(computer_graph[cur])
            is_visited[cur] = True
            result += 1

    print(result - 1)

dfs()
