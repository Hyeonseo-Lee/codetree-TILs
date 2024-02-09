a = int(input())
arr = list(map(int, input().split()))
idx = a + 1
ans = []
for j in range(1000):
    if idx == 1:
        break   
    max_val = 0
    for i in range(0,idx - 1):
        if arr[i] > max_val:
            idx = i + 1
            
            max_val = arr[i]
        # print(f'i={i}, idx={idx},max_val={max_val} ')
    arr = arr[:idx - 1]
    ans.append(idx)
    # print(f'arr={arr}')
    # print(f'ans={ans}')
print(*ans, sep = ' ')