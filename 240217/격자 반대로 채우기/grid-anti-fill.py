n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]

for j in range(n-1, -1, -2):
    cnt = (n - 1 - j) * n + 1
    for i in range(n-1, -1, -1):
        arr[i][j] = cnt
        cnt += 1

for j in range(n-2, -1, -2):
    cnt = (n - 1 - j) * n + 1
    for i in range(0,n):
        arr[i][j] = cnt
        cnt += 1

for i in range(n):
    print(*arr[i], end = ' ')
    print()