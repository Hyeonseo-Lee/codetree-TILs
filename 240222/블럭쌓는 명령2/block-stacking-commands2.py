n, k = map(int, input().split())
arr = [0 for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    for i in range(a-1, b):
        arr[i] += 1

max_val = arr[0]

for i in range(k):
    if arr[i] > max_val:
        max_val = arr[i]
print(max_val)