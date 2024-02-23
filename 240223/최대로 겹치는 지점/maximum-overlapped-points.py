n = int(input())
arr = [0] * 100
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a-1, b):
        arr[i] += 1


max_val = arr[0]
for i in range(100):
    if arr[i] > max_val:
        max_val = arr[i]
print(max_val)