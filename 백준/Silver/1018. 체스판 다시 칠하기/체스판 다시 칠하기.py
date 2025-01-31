n, m = map(int, input().split())

board_b = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB'
]

board_w = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]

b_cnt = 2501
w_cnt = 2501

board_state = []

for _ in range(n):
    board_state.append(input())

def cnt_b(x, y):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if board_state[x + i][y + j] != board_b[i][j]:
                cnt += 1

    return cnt

def cnt_w(x, y):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if board_state[x + i][y + j] != board_w[i][j]:
                cnt += 1

    return cnt

for x in range(n - 7):
    for y in range(m - 7):
        b_cnt = min(cnt_b(x, y), b_cnt)
        w_cnt = min(cnt_w(x, y), w_cnt)

print(min(b_cnt, w_cnt))
