result = [0, 1, 2]

for i in range(3, 1001):
    result.append(result[i - 1] + result[i - 2])

n = int(input())

print(result[n] % 10007)
