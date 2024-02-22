n = int(input())
arr = [0 for _ in range(201)]
for _ in range(n):
    a, b = map(int, input().split())
    a, b = a + 100, b + 100
    for i in range(a, b):
        arr[i] += 1

max_val = arr[i]
for i in range(201):
    if arr[i] > max_val:
        max_val = arr[i]
print(max_val)