n, t = map(int, input().split())
x, y, d = input().split()
x, y = int(x), int(y)
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
mapper = {'U': 2, 'D': 1, 'R': 0, 'L': 3}
direc = mapper[d]
def in_range(x, y):
    return x > 0 and x <= n and y > 0 and y <= n

for i in range(t):
    nx, ny = x + dxs[direc], y + dys[direc]
    if not in_range(nx, ny):
        direc = 3 - direc
    else:
        x, y = x + dxs[direc], y + dys[direc]
    # print(f'i: {i}, nx: {nx}, ny: {ny}, direc: {direc}')
    # print(f'i: {i}, x: {x}, y: {y}, direc: {direc}')

print(x, y)