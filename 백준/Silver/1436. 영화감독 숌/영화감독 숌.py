n = int(input())

dooms_day = 666
series = 0

while(True):
    dooms_day_str = str(dooms_day)

    for j in range(len(dooms_day_str) - 2):
        if dooms_day_str[j] == '6' and dooms_day_str[j + 1] == '6' and dooms_day_str[j + 2] == '6':
            series += 1
            break
    
    if series == n:
        break

    dooms_day += 1

print(dooms_day_str)