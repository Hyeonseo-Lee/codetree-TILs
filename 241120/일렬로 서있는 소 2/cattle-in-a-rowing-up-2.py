n = int(input())
data = list(map(int, input().split()))
num = 0

for i in range(n):
    for j in range(i + 1, n):
        if data[j] >= data[i]:
            for k in range(j + 1, n):
                if data[k] >= data[j]:
                    num = num + 1

print(num)


