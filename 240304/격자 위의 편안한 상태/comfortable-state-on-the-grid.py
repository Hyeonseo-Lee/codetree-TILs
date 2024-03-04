n, m = map(int, input().split())
arr = [[0] * n for _ in range(n)]
dxs, dys = [0, -1, 0, 1],[1, 0, -1, 0]
def is_number(x, y):
    return x >= 0 and x < n and y >= 0 and y < n
for _ in range(m):
    ans, cnt = 0, 0
    r, c = map(int, input().split())
    arr[r - 1][c - 1] = 1
    for i, j in zip(dxs, dys):
        nx, ny = r + i - 1, c + j -1
        if is_number(nx, ny):
            if arr[nx][ny] == 1:
                cnt += 1
    if cnt == 3:
        ans = 1
    print(ans)