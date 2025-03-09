a, b = map(int, input().split())
grid = [list(input().split()) for _ in range(b)]
cnt = 0
answer = 0

for i in range(1, b-1):
    for j in range(1, a-1):
        for k in range(i+1, b-1):
            for g in range(j+1, a-1):
                if grid[i][j] != grid[k][g]:
                    cnt += 1
                if cnt == 2:
                    answer += 1
                    break

print(answer)