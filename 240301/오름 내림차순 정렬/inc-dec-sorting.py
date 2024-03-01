n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(*arr, end = ' ')
arr = arr[::-1]
print()
print(*arr, end = ' ')