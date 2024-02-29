n = int(input())
arr = [[0] * 2001 for _ in range(2001)]

for k in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + 100, y1 + 100, x2 + 100, y2 + 100

    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = k
cnt = 0
for i in range(2001):
    for j in range(2001):
        if arr[i][j] == 1:
            cnt += 1
print(cnt)