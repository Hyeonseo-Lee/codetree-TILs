sen = input()
x, y, cnt = 0, 0, 0
c_dir = 0
ans = -1
# 북 -> 동
# 동 -> 남
# 남 -> 서
# 서 -> 북
# 북 -> 서
# 서 -> 남
# 남 -> 동 
# 동 -> 북
# 북 동 남 서 
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
for i in sen:
    #print(f'i: {i}, x: {x}, y: {y}, c_dir: {c_dir}, cnt: {cnt}')
    if i == 'F':
        x, y = x + dxs[c_dir], y + dys[c_dir]
        cnt += 1
    elif i == 'R':
        c_dir = (c_dir + 1) % 4        
        cnt += 1
    elif i == 'L':
        c_dir = (c_dir + 3) % 4      
        cnt += 1
    if x == 0 and y == 0:
        ans = cnt
        break
    
print(ans)