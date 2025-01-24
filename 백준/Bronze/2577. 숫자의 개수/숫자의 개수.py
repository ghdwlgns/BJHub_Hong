cnts = [0 for i in range(10)]

result = 1
for _ in range(3):
    result *= int(input())

while result != 0:
    cnts[result % 10] += 1
    result = result // 10

for c in cnts:
    print(c)