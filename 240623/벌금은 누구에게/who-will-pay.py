n, m, k = map(int, input().split())
arr = [0]*n

for i in range(m):
    s = int(input())
    arr[s-1] += 1
    if arr[s-1] == k:
        print(s)
        break