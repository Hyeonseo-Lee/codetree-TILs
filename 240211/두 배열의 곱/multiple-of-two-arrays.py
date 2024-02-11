arr = [list(map(int, input().split())) for _ in range(7)]
narr = [[] for _ in range(3)]
for i in range(3):
    for j in range(3):
        narr[i].append(arr[i][j] * arr[i+4][j])
for i in range(3):
    print(*narr[i], sep = ' ')