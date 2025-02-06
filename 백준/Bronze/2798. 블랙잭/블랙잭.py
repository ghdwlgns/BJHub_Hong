n, m = map(int, input().split())

card_list = [i for i in map(int, input().split())]

total = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            sum = card_list[i] + card_list[j] + card_list[k]
            if sum <= m:
                total = max(total, sum)
                
print(total)
