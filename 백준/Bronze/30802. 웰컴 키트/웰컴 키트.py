import sys

n = int(input())

t_list = [int(i) for i in sys.stdin.readline().split()]

t, p = map(int, input().split())

t_set = 0

for x in t_list:
    if x % t != 0:
        t_set = t_set + x // t + 1
    else:
        t_set += x // t

print(t_set)
print(f'{n // p} {n % p}')
