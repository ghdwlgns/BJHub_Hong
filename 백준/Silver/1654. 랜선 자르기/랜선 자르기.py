k, n = map(int, input().split())

line_list = []

for _ in range(k):
    line_list.append(int(input()))

left, right = 1, max(line_list)
result = 0

while left <= right:
    mid = (left + right) // 2
    total = sum(l // mid for l in line_list)
    
    if total >= n:
        result = mid if result < mid else result
        left = mid + 1
    else:
        right = mid - 1

print(result)
