from collections import deque

n = int(input())
card_queue = deque(range(1, n + 1))

while len(card_queue) > 1:
    card_queue.popleft()
    card_queue.append(card_queue.popleft())

print(card_queue.popleft())
