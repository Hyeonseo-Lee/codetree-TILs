n = int(input())
arr = []
cnt = 0
max_cnt = 0
for i in range(n):
    #print(f'arr:{arr},cnt: {cnt}, max_cnt: {max_cnt}')
    arr.append(int(input()))
    if i == 0 or arr[i] == arr[i - 1]:
        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    else:
        cnt = 1

print(max_cnt)