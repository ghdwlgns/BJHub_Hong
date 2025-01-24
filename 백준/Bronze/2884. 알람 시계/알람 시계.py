timer = input().split()

hour = int(timer[0])
minute = int(timer[1]) - 45

if minute >= 0:
    print(f'{hour} {minute}')
elif hour - 1 >= 0:
    print(f'{hour - 1} {60 + minute}')
else:
    print(f'23 {60 + minute}')