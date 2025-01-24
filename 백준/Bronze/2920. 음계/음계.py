chords = [int(c) for c in input().split()]

is_ascending = True
is_descending = True

for i in range(7):
    if i == 0 and chords[i] == 1:
        is_descending = False
    elif i == 0 and chords[i] == 8:
        is_ascending = False

    elif chords[i] < chords[i + 1] and is_descending:
        is_ascending = False
        is_descending = False
        break

    elif chords[i] > chords[i + 1] and is_ascending:
        is_descending = False
        is_ascending = False
        break

if is_ascending:
    print('ascending')
elif is_descending:
    print('descending')
else:
    print('mixed')
