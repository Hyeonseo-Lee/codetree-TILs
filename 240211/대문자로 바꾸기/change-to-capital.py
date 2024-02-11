narr = [[] for _ in range(5)]
arr = [list(input().split()) for _ in range(5)]

for i in range(5):
    for j in range(3):
        narr[i].append(arr[i][j].upper())
    print(*narr[i], sep = ' ')