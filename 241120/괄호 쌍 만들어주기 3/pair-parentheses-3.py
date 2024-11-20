data = list(input())
n = len(data)
sum = 0

for i in range(n):
    if data[i] == '(':
        for j in range(i+1, n):
            if data[j] == ')':
                sum = sum + 1
print(sum)
