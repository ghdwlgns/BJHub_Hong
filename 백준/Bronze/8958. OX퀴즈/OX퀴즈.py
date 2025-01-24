t = int(input())

for _ in range(t):
    score = 0
    semi_score = 0
    
    result = input()

    for c in result:
        if c == 'O':
            semi_score += 1
            score += semi_score
        else:
            semi_score = 0

    print(score)
