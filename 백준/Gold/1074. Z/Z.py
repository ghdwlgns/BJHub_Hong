n, r, c = map(int, input().split())

result = 0

while n >= 0:
    if 0 <= r < 2 ** (n - 1) and 0 <= c < 2 ** (n - 1):
        # 1사분면에 위치
        pass
    elif 0 <= r < 2 ** (n - 1) and 2 ** (n - 1) <= c < 2 ** n:
        # 2 사분면에 위치
        result += 4 ** (n - 1)
        c -= 2 ** (n - 1)
    elif 2 ** (n - 1) <= r < 2 ** n and 0 <= c < 2 ** (n - 1):
        # 3 사분면에 위치
        result += 2 * 4 ** (n - 1)
        r -= 2 ** (n - 1)
    else:
        # 4 사분면에 위치
        result += 3 * 4 ** (n - 1)
        r -= 2 ** (n - 1)
        c -= 2 ** (n - 1)
    n -= 1

print(result)
