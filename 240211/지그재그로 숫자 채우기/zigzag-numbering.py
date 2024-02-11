n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
sum_val = 0
for j in range(m):
    if j % 2 == 0:
        for i in range(n):
            arr[i][j] += sum_val
            sum_val += 1
    else:
        for i in range(n-1, -1, -1):
            arr[i][j] += sum_val
            sum_val += 1
for i in range(n):
    print(*arr[i], sep = ' ')