def printrectangle(n, m):
    for _ in range(n):
        print('1' * m)

n, m = map(int, input().split())
printrectangle(n, m)