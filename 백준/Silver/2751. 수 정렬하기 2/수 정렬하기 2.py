import sys
import heapq

n = int(input())

numbers = [int(sys.stdin.readline()) for _ in range(n)]
heapq.heapify(numbers)

print('\n'.join(map(str, (heapq.heappop(numbers) for _ in range(n)))))