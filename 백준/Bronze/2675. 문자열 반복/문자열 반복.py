t = int(input())

for _ in range(t):
    result = ''
    i = input()
    r = int(i.split()[0])
    s = i.split()[1]

    for c in s:
        for _ in range(r):
            result += c

    print(result)