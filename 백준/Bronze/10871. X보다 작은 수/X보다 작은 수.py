n, x = map(int, input().split())

nums = map(int, input().split())

result = []

for i in nums:
    if i < x:
        result.append(i)

result = ' '.join(map(str, result))
print(result)
