import sys

# 입력 받기
n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

# ✅ 누적 합(Prefix Sum) 배열 생성 (`O(N)`)
prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

# ✅ 입력을 리스트에 저장 (`O(M)`)
queries = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

# ✅ 빠른 출력 (`O(M)`)
sys.stdout.write("\n".join(str(prefix_sum[j] - prefix_sum[i - 1]) for i, j in queries) + "\n")
