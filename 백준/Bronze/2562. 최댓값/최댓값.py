max_num = -1
max_index = 0

for i in range(1, 10):
    num = int(input())
    if max_num < num:
        max_num = num
        max_index = i

print(max_num)
print(max_index)