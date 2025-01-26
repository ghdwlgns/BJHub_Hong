n = int(input())

strings = set()

for _ in range(n):
    strings.add(input())

result = sorted(strings, key=lambda x: (len(x), x))

for s in result:
    print(s)