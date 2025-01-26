inputs = [string for string in iter(input, '0')]

def is_palindrome(num):
    for i in range(len(num) // 2):
        if num[i] != num[len(num) - 1 - i]:
            return 'no'
    
    return 'yes'

for num in inputs:
    print(is_palindrome(num))