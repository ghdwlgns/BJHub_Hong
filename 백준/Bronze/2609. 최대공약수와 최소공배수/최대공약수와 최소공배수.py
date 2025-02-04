import math

m, n = map(int, input().split())

gcd = math.gcd(m, n)
lcm = (m * n) // gcd

print(gcd)
print(lcm)
