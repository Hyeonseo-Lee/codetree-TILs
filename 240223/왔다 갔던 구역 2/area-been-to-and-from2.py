n = int(input())
arr = [0] * 2001
start = 1000
for _ in range(n):
    a, b = input().split()
    a = int(a)
    
    if b == 'R':
        for i in range(start, start + a):
            arr[i] += 1
            start = start + a
        # print(f'start: {start}, a: {a}, b: {b}')
    if b == 'L':
        for i in range(start, start - a, -1):
            arr[i] += 1
            start = start - a
        # print(f'start: {start}, a: {a}, b: {b}')

cnt = 0
for i in range(2000):
    if arr[i] >= 2:
        cnt += 1
print(cnt)