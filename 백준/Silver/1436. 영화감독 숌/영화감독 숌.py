n = int(input())

dooms_day = 666
series = 0

while(True):
    if '666' in str(dooms_day):
        series += 1
    
    if series == n:
        break

    dooms_day += 1

print(dooms_day)