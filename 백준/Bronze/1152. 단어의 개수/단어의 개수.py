_input = input()

split_by_blank = _input.split(" ")

if split_by_blank[-1] == '' and split_by_blank[0] == '':
    print(len(split_by_blank) - 2)
elif split_by_blank[-1] == '':
    print(len(split_by_blank) - 1)
elif split_by_blank[0] == '':
    print(len(split_by_blank) - 1)
else:
    print(len(split_by_blank))