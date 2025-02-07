from collections import deque

n, k = map(int, input().split())

circular_queue = deque([i for i in range(1, n + 1)], maxlen=n)
result = []

while circular_queue:
    circular_queue.rotate(-(k - 1))
    result.append(str(circular_queue.popleft()))

print(f"<{', '.join(result)}>")
