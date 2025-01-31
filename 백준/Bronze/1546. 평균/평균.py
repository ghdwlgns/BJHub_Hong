n = int(input())

scores = [n for n in iter(map(int, input().split()))]

new_scores = [n / max(scores) * 100 for n in scores]

print(sum(new_scores) / len(new_scores))