a, b = map(int, input().split())
max_val = 1
for i in range(1, 101):
    if a % i == 0 and b % i == 0 and i > max_val:
        max_val = i
print(max_val)