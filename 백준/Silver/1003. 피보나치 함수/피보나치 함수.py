t = int(input())

result = [(1, 0), (0, 1)]

for i in range(2, 41):
    result.append(tuple(a + b for a, b in zip(result[i - 1], result[i - 2])))

for _ in range(t):
    print(*result[int(input())])
