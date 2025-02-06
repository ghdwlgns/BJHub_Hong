from collections import deque

n = int(input())

for _ in range(n):
    p_str = deque()
    for c in input():
        if c == '(':
            p_str.append(c)
        else:
            if len(p_str) == 0:
                p_str.append(c)
                break
            p_str.pop()
    
    if len(p_str) > 0:
        print("NO")
    else:
        print("YES")