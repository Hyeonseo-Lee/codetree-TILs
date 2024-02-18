n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        cnt += 1
        arr[i][j] = cnt
        if cnt == 9:
            cnt = 0
for i in range(n):
    print(*arr[i], end = ' ')
    print()