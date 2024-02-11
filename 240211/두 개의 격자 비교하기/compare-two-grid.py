a, b = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(a)]
arr2 = [list(map(int, input().split())) for _ in range(a)]
ans = [[0 for _ in range(b)] for _ in range(a)]
for i in range(a):
    for j in range(b):
        if arr1[i][j] != arr2[i][j]:
            ans[i][j] = 1
    print(*ans[i], sep = ' ')