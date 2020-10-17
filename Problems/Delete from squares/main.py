key = int(input())
if squares.get(key) is None:
    print('There is no such key')
else:
    print(squares.get(key))
    del squares[key]
