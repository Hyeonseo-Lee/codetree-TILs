n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
ncnt = 0
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

for x in range(n):
    for y in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            x, y = x + dx, y + dy
            if in_range(x, y) and arr[x][y] == 1:
                cnt += 1
            x, y = x - dx, y - dy
        if cnt >= 3:
            ncnt += 1
print(ncnt)