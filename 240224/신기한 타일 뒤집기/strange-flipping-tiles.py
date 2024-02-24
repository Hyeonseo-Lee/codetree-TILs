n = int(input())
arr = [0] * 200001
start = 100000
for _ in range(n):
    a, b = input().split()
    a = int(a)

    if b == 'L':
        for i in range(start, start -a,  -1):
            arr[i] = 1
        start = start - a + 1

    if b == 'R':
        for i in range(start, start + a):
            arr[i] = 2
        start = start + a - 1
    #print(f'start: {start}, a: {a}, b: {b}')
cnt1, cnt2 = 0, 0

for i in range(200001):
    if arr[i] == 1:
        cnt1 += 1
    if arr[i] == 2:
        cnt2 += 1
print(cnt1, cnt2)