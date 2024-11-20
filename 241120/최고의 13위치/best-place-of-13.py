import sys
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
minv = -sys.maxsize

for i in range(n):
    for j in range(n - 2):
        num = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
        # print(num)
        if num > minv:
            minv = num
print(minv)
        