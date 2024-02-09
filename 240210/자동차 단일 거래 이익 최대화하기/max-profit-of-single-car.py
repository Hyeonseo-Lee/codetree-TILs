a = int(input())
arr = list(map(int, input().split()))
max_val = 0
for i in range(a):
    for j in range(i, a):
        if arr[i] < arr[j] and arr[j] - arr[i] > max_val:
            max_val = arr[j] - arr[i]
print(max_val)