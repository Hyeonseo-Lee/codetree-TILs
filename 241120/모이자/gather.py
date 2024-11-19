import sys
n = int(input())
data = list(map(int, input().split()))

min_sum = sys.maxsize
for i in range(n):
    sum = 0
    for j in range(n):
        sum = sum + data[j] *abs(j - i)
    if sum < min_sum:
        min_sum = sum

print(min_sum)
