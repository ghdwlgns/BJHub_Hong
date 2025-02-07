import sys
from collections import Counter

result = []
n = input()
deck = [x for x in sys.stdin.readline().split()]
deck_count = Counter(deck)

m = input()
for num in sys.stdin.readline().split():
    if deck_count[num]:
        result.append(deck_count[num])
    else:
        result.append(0)

print(' '.join(str(n) for n in result))