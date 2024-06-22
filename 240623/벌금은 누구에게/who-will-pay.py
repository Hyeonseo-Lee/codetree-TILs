n, m, k = map(int, input().split())
arr = [0]*n
ans = -1
for i in range(m):
    s = int(input())
    arr[s-1] += 1
    if arr[s-1] == k:
        ans = s
        break
print(ans)