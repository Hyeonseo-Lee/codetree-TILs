n = int(input())
arr = [int(input()) for _ in range(n)]
max_cnt = 0
for i in range(n):
    if i != 0 and arr[i] * arr[i - 1] > 0:
        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    else:
        cnt = 1
print(max_cnt)