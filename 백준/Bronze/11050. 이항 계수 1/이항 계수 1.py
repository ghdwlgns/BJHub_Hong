def combination(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    else:
        k = min(k, n - k)
        denom = 1
        numer = 1
        for _ in range(k):
            denom *= n
            numer *= k
            n -=1
            k -=1

        return denom // numer

n, k = map(int, input().split())

print(combination(n, k))
