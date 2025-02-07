t = int(input())

result = [(1, 0), (0, 1)] + [None] * 39

for i in range(2, 41):
    result[i] = (result[i - 1][0] + result[i - 2][0], result[i - 1][1] + result[i - 2][1])

for _ in range(t):
    print(*result[int(input())])
