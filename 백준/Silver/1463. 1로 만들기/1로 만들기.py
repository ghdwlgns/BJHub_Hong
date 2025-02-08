result = [None] + [0] * 1000000

for i in range(2, 1000001):
    result[i] = result[i - 1] + 1
    if i % 2 == 0:
        result[i] = min(result[i], result[i // 2] + 1)
    if i % 3 == 0:
        result[i] = min(result[i], result[i // 3] + 1)

n = int(input())
print(result[n])
