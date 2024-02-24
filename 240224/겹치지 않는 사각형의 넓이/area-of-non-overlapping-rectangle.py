arr = [[0] * 2001 for _ in range(2001)]
checked = [list(map(int, input().split())) for _ in range(3)]

for k in range(3):
    for i in range(checked[k][0] + 1000, checked[k][2] + 1000):
        for j in range(checked[k][1] + 1000, checked[k][3] + 1000):
            if k == 2:
                arr[i][j] = 2
            else:
                arr[i][j] = 1
cnt = 0

for k in range(2):
    for i in range(checked[k][0] + 1000, checked[k][2]+1000):
        for j in range(checked[k][1]+1000, checked[k][3]+1000):
            if arr[i][j] == 1:
                cnt += 1
print(cnt)