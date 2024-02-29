n, m = map(int, input().split())
a_arr, b_arr = [0] * 1001, [0] * 1001

def findtime(nm, arr):
    start, place = 0, 0
    for _ in range(nm):
        d, t = input().split()
        t = int(t)
        if d == 'R':
            for i in range(start+1, start + t + 1):
                place += 1     
                arr[i] = place   
        else:
            for i in range(start+1, start + t + 1):
                place -= 1
                arr[i] = place
            
        start = start + t
        #print(f'd: {d}, t: {t}, start: {start}, place:{place}')
   
findtime(n, a_arr)
findtime(m, b_arr)

ans = -1
for i in range(1001):
    if a_arr[i] != 0 and a_arr[i] == b_arr[i]:
        ans = i
        break
print(ans)