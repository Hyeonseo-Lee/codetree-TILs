x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
dir_num = 3
dist = 0
for i in input():
    
    if i == 'L':
        dir_num = (dir_num + 3) % 4
    elif i == 'R':
        dir_num = (dir_num + 1) % 4
    elif i == 'F':
        dist = 1
    x, y = x + dx[dir_num] * dist, y + dy[dir_num] * dist
print(x, y)