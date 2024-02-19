n, m = map(int, input().split())
wherestop = True
for i in range(1, m):
    val1 = n * i
    for j in range(1, n):
        val2 = m * j
        if val1 == val2:
            wherestop = False
            break
    if wherestop == False:
        print(val1)
        break