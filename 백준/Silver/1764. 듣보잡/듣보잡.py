import sys

n, m = map(int, input().split())

who_the_heck_list = {sys.stdin.readline().strip() for _ in range(n)}

total_unknowns = sorted(never_seen_before for _ in range(m) if (never_seen_before := sys.stdin.readline().strip()) in who_the_heck_list)

print(len(total_unknowns))
print('\n'.join(name for name in total_unknowns))