from collections import deque

n = int(input())

for _ in range(n):
    p_str = deque()
    is_valid = True
    for c in input():
        if c == '(':
            p_str.append(c)
        else:
            if not p_str:
                is_valid = False
                break
            p_str.pop()
            
    print("YES" if is_valid and not p_str else "NO")