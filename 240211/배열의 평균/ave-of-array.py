arr = [list(map(int, input().split())) for _ in range(2)]
narr = [[] for _ in range(2)]

for i in range(2):
    narr[0].append(sum(arr[i]) / 4)
for i in range(4):
    narr[1].append((arr[0][i] + arr[1][i]) / 2)
for i in range(2):
    print(*narr[i], sep = ' ')
print(f'{(narr[0][0] + narr[0][1]) / 2:.1f}')