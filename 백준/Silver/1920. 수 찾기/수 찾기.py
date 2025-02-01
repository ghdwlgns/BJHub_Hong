n = int(input())

num_set = {int(i) for i in input().split()}

m = int(input())

cmp_list = list(map(int, input().split()))

print('\n'.join('1' if i in num_set else '0' for i in cmp_list))