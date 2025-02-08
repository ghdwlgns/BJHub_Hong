from collections import deque

n, k = map(int, input().split())

field = [0] * 100001

def bfs():
    coord_list = deque()
    coord_list.append(n)

    field[n] = 1

    while coord_list:
        x = coord_list.popleft()
        
        if x == k:
            break
        if x + 1 <= 100000 and field[x + 1] == 0:
            coord_list.append(x + 1)
            field[x + 1] = field[x] + 1
        
        if x - 1 >= 0 and field[x - 1] == 0:
            coord_list.append(x - 1)
            field[x - 1] = field[x] + 1

        if 2 * x <= 100000 and field[2 * x] == 0:
            coord_list.append(2 * x)
            field[2 * x] = field[x] + 1

    return field[k] - 1

print(bfs())
