n = int(input())
arr = [0] * 2001
start = 1000
for _ in range(n):
    a, b = input().split()
    a = int(a)
    
    if b == 'R':
        #print(f'start: {start}, a: {a}, b: {b}')
        for i in range(start, start + a):
            arr[i] += 1
        start = start + a 
        
    if b == 'L':
        # print(f'start: {start}, a: {a}, b: {b}')
        for i in range(start - a, start):
            arr[i] += 1
        start = start - a
        

cnt = 0
for i in range(2000):
    if arr[i] >= 2:
        cnt += 1


print(cnt)