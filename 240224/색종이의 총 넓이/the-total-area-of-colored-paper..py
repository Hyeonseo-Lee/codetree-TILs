n = int(input())
arr =[[0] * 201 for _ in range(201)]
for _ in range(n):
    a, b = map(int, input().split())
    a, b = a + 100, b + 100

    for i in range(a, a + 8):
        for j in range(b, b + 8):
            arr[i][j] = 1

cnt = 0
for i in range(201):
    for j in range(201):
        if arr[i][j] == 1:
            cnt += 1
print(cnt)