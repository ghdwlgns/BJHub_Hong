from collections import deque

n, k = map(int, input().split())

circular_queue = deque([i for i in range(1, n + 1)], maxlen=n)
result = "<"

cnt = 1

while circular_queue:
    if cnt == k:
        cnt = 1
        result += str(circular_queue.popleft()) + ", "
    else:
        circular_queue.append(circular_queue.popleft())
        cnt += 1

result = result[:-2] + ">"
print(result)
