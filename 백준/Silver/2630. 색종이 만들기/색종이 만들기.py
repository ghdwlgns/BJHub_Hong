import sys

n = int(input())

paper_state = [[int(c) for c in sys.stdin.readline().split()] for _ in range(n)]

def partition(p, x, y, size):
    
    c = p[x][y]

    is_all_same = True

    for i in range(x, x + size):
        for j in range(y, y + size):
            if p[i][j] != c:
                is_all_same = False
                break
        if not is_all_same:
            break

    if is_all_same:
        return (1, 0) if c == 1 else (0, 1)
    
    size //= 2
    b1, w1 = partition(p, x, y, size)
    b2, w2 = partition(p, x, y + size, size)
    b3, w3 = partition(p, x + size, y, size)
    b4, w4 = partition(p, x + size, y + size, size)

    return (b1 + b2 + b3 + b4, w1 + w2 + w3 + w4)

result_b, result_w = partition(paper_state, 0, 0, n)

print(result_w)
print(result_b)
