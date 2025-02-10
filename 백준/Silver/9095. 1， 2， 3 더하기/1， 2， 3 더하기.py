import sys

result = [0, 1, 2, 4] + [None] * 7

for i in range(4, 11):
    result[i] = result[i - 1] + result[i - 2] + result[i - 3]

t = int(input())

print('\n'.join(str(result[int(sys.stdin.readline().strip())]) for _ in range(t)))
