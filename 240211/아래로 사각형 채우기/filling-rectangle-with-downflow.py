n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
sum_val = 1

for i in range(n):
    for j in range(n):
        arr[j][i] += sum_val
        sum_val += 1
for i in range(n):
    print(*arr[i], sep = ' ')