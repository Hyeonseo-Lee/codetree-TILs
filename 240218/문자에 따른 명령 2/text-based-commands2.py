x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
dir_num = 3

for i in input():
    dist = 0
    if i == 'L':
        dir_num = (dir_num + 3) % 4
    elif i == 'R':
        dir_num = (dir_num + 1) % 4
    elif i == 'F':
        dist = 1
    
    x, y = x + dx[dir_num] * dist, y + dy[dir_num] * dist
    # print(f'x:{x}, y:{y}, dist: {dist}, dir_num: {dir_num}, i:{i}')
print(x, y)