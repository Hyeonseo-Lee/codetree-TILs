a = int(input())
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

for i in range(a):
    
    dirchr, c = input().split()
    if dirchr == 'E':
        x, y = x + dx[0] * int(c), y + dy[0] * int(c)
    elif dirchr == 'S':
        x, y = x + dx[1] * int(c), y + dy[1] * int(c)
    elif dirchr == 'W':
        x, y = x + dx[2] * int(c), y + dy[2] * int(c)
    else:
        x, y = x + dx[3] * int(c), y + dy[3] * int(c)
    # print(f'x: {x}, y: {y}, i: {i}, c: {c}')
print(x, y)