while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except ValueError and EOFError:
        break