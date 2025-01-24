s = input()

alphabet_cnt_list = [-1 for _ in range(26)]

for i, c in enumerate(s):
    c_to_i = ord(c) - 97
    if alphabet_cnt_list[c_to_i] == -1:
        alphabet_cnt_list[c_to_i] = i

result = ' '.join(map(str, alphabet_cnt_list))
print(result)