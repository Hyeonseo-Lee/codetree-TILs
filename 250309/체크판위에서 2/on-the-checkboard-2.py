a, b = map(int, input().split())
grid = [list(input().split()) for _ in range(a)]
cnt = 0
answer = 0

for i in range(a):
    for j in range(b):
        for k in range(i+1, a-1):
            for g in range(j+1, b-1):
                  
                if grid[i][j] != grid[0][0] and grid[k][g] != grid[i][j] and grid[k][g] != grid[a-1][b-1]:
                    cnt += 1
                    #print(i,j,grid[i][j],k,g,grid[k][g],cnt)
                            

print(cnt)
