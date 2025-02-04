m, n = map(int, input().split())

def lcm(x, y):
    (x, y) = (max(x, y), min(x, y))
    (a, b) = (x, y)
    

    while y > 0:
        r = x % y
        x, y = y, r
    
    g = x

    return (a * b) // g, g

l, g = lcm(m, n)

print(g)
print(l)
