import heapq
import sys

num_heap = []
n = int(input())

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        print(heapq.heappop(num_heap) if num_heap else 0)
    else:
        heapq.heappush(num_heap, x)
