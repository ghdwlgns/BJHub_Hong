import sys
import heapq

n = int(input())

coords_data = map(int, sys.stdin.readline().split())
coord_dic = {}

for index, coord in enumerate(coords_data):
    coord_dic.setdefault(coord, []).append(index)

heap = [(-key, value) for key, value in coord_dic.items()]
heapq.heapify(heap)

result = [0] * n

while heap:
    x, index = heapq.heappop(heap)
    for i in index:
        result[i] = len(heap)

print(*result)
