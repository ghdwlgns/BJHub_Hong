n, r, c = map(int, input().split())

result = 0
size = 2 ** (n - 1) # 초기 탐색할 정사각형 배열(행렬) 한 변 길이

while size > 0:
    quadrant = (r >= size) * 2 + (c >= size)
    result += quadrant * size ** 2
    
    r %= size
    c %= size
    size //= 2

print(result)
