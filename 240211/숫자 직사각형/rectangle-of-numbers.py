n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
sum_val = 0
for i in range(n):
    for j in range(m):
        sum_val += 1
        arr[i][j] += sum_val

for i in range(n):
    print(*arr[i], sep = ' ')