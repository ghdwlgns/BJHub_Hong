year = int(input())

if year % 100 == 0 and year % 400 != 0 or year % 4 != 0:
    print(0)
else:
    print(1)