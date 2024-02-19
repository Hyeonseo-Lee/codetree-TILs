n, m = map(int, input().split())
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
arr = [[0] * n for _ in range(m)]
arr[0][0] = 1
x, y, direct = 0, 0, 0
def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

for i in range(2, n ** 2 + 1):
    nx, ny = x + dxs[direct], y + dys[direct]
    if not in_range(nx, ny) or arr[nx][ny] != 0:
        direct = (direct + 1) % 4
    x, y = x + dxs[direct], y + dys[direct]
    arr[x][y] = i

for i in range(n):
    print(*arr[i], end = ' ')
    print()