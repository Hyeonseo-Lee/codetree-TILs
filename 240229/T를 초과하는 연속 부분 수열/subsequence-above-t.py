n, t = map(int, input().split())
arr = list(map(int, input().split()))

cnt, max_cnt = 0, 0
for i in range(n):
    if arr[i] > t:
        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    else:
        cnt = 0

print(max_cnt)