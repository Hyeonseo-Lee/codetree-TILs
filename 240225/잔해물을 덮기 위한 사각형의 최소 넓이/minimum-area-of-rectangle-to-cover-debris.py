arr = [[0] * 2001 for _ in range(2001)]
for k in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + 1000, y1 + 1000, x2 + 1000, y2 + 1000
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = k + 1
min_xval, max_xval, min_yval, max_yval = 2000, 0, 2000, 0
for i in range(2001):
    for j in range(2001):
        if arr[i][j] == 1:
            if i < min_xval:
                min_xval = i
            if j < min_yval:
                
                min_yval = j
            if  i > max_xval:
                max_xval = i
            if j > min_yval:
                
                max_yval = j
#print(min_xval, max_xval, min_yval, max_yval)
if max_xval >= min_xval and max_yval >= min_yval:
    print((max_xval - min_xval + 1) * (max_yval - min_yval + 1)) 
else:
    print(0)