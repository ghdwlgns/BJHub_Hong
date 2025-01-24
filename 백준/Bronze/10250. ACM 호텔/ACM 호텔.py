t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())

    if n % h != 0:
        floor = n % h
        room = n // h + 1
    else:
        floor = h
        room = n // h

    if room < 10:
        print(f'{floor}0{room}')
    else:
        print(f'{floor}{room}')