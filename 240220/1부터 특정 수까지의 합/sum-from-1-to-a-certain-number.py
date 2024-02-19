n = int(input())
s = 0
def getvalue(n):
    global s
    for i in range(1, n + 1):
        s += i
    return s // 10
v = getvalue(n)
print(v)