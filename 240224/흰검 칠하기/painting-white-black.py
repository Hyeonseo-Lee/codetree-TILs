n = int(input())
arr = [[0, 0, 0] for _ in range(200001)]
start = 100000

for _ in range(n):
    a, b = input().split()
    a = int(a) 
    if b == 'R':
        for i in range(start, start + a):
            arr[i][1] += 1
            if arr[i][1] >= 2 and arr[i][2] >= 2:
                arr[i][0] = 3
                
            else:
                arr[i][0] = 1
                
        start = start + a
    elif b == 'L':
        for i in range(start - a, start):
            arr[i][2] += 1
            if arr[i][1] >= 2 and arr[i][2] >= 2:
                arr[i][0] = 3
            else:  
                arr[i][0] = 2
                
        start = start - a
    #print(f'start: {start}, a: {a}, b: {b}')
cnt1, cnt2, cnt3 = 0, 0, 0
for i in range(200001):
    if arr[i][0] == 1:
        cnt1 += 1
    if arr[i][0] == 2:
        cnt2 += 1
    if arr[i][0] == 3:
        cnt3+= 1
print(cnt2, cnt1, cnt3)
# for i in range(99900, 100100):
#     print(arr[i][0], end = ' ')