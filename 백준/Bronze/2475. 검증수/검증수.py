line = input()
sum = 0

nums = [int(c) for c in line.split()]

for n in nums:
    sum += n**2

print(sum % 10)