import sys

m = int(input())

num_set = set()

for _ in range(m):
    op = sys.stdin.readline()
    if 'add' in op:
        x = int(op.split()[1])
        num_set.add(x)
    elif 'remove' in op:
        x = int(op.split()[1])
        num_set.discard(x)
    elif 'check' in op:
        x = int(op.split()[1])
        print(1 if x in num_set else 0)
    elif 'toggle' in op:
        x = int(op.split()[1])
        if x in num_set:
            num_set.remove(x)
        else:
            num_set.add(x)
    elif 'all' in op:
        num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    else:
        num_set = set()
