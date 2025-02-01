n = input()

def isPrime(n):
    if n == 1:
        return False
    
    for i in range(2, n // 2 + 1):
        if n != i and n % i == 0:
            return False
    return True

cnt = 0

for i in iter(map(int, input().split())):
    if isPrime(i):
        cnt += 1

print(cnt)
