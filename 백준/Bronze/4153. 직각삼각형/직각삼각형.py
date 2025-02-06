while True:
    side_list = sorted(map(int, input().split()))

    if 0 in side_list:
        break
    elif side_list[0]**2 + side_list[1]**2 == side_list[2]**2:
        print('right')
    else:
        print('wrong')

