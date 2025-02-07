from collections import deque
import sys

n = int(input())
stack = deque()

for _ in range(n):
    op = sys.stdin.readline().strip()
    if "push" in op:
        stack.append(op.split()[1])
    elif op == "pop":
        if not stack:
            print(-1)
        else:
            x = stack.pop()
            print(x)
    elif op == "size":
        print(len(stack))
    elif op == "empty":
        print(0 if stack else 1)
    elif op == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
