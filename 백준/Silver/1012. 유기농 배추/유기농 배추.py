t = int(input())

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
for _ in range(t):
    m, n, k = map(int, input().split())
    field = {tuple(map(int, input().split())) for _ in range(k)}

    def dfs(x, y):
        st = [(x, y)]
        while st:
            tx, ty = st.pop()
            if (tx, ty) in field:
                field.remove((tx, ty))
                for dx, dy in directions:
                    st.append((tx + dx, ty + dy))

    cnt = 0
    while field:
        x, y = next(iter(field))
        dfs(x, y)
        cnt += 1
    
    print(cnt)
