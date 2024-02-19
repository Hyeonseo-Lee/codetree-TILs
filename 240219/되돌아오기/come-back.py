n = int(input())
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
ans = -1
mapper = {'W': 2, 'S': 1, 'N': 3, 'E': 0 }
x, y, cnt = 0, 0, 0
# arr과 초기 x, y를 설정할 때
# 북으로 얼마 갔는지, 총 세로 길이
# 서로 얼마나 갔는지, 총 가로 길이
# 총 세로 * 총 가로 = arr 
# 북으로 얼마 갔는지, 서로 얼마 갔는지 초기 x, y로 
whenbreak = True
for i in range(n):
    dir_chr, move_val = input().split()
    move_val = int(move_val)
    dir_chr = mapper[dir_chr]
    for j in range(move_val):
        
        x, y = x + dxs[dir_chr], y + dys[dir_chr] 
        cnt += 1
        # print(f'x: {x}, y: {y}, dir_chr:{dir_chr}')
        if x == 0 and y == 0:
            whenbreak = False
            break
    if whenbreak == False:
        ans = cnt
        break
print(ans)