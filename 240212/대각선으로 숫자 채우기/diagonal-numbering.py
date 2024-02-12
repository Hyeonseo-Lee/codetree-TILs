n, m = map(int, input().split())

arr = [[0 for _ in range(m)] for _ in range(n)]
sum_val = 1
arr[0][0] = sum_val
i, j,k = 0, 0,0

while True:
    # print(i, j, sum_val)
    if i == n -1 and j == m -1 :
        # print("6들어옴")
        break
    elif i == n - 1 and j == m - 2:
        # print("1들어옴")
        j += 1
        sum_val += 1
        arr[i][j] = sum_val
        break
    elif j - 1 <0 and arr[0][m-1] > 0 or arr[0][m-1]>0 and i == n -1:
        # print("4들어옴")
        k += 1
        i = k
        j = m - 1
        sum_val += 1
        arr[i][j] = sum_val
    elif j - 1 <0 :
        # print("2들어옴")
        j = i + 1
        i = 0
        sum_val += 1
        arr[i][j] = sum_val
    elif n == 1:
        j = j + 1
        sum_val += 1
        arr[i][j] = sum_val
    elif i == n - 1 and arr[i][j] > 0:
        # print("5들어옴")
        i = 0
        j = m -1
        sum_val += 1
        arr[i][j] = sum_val   
    elif j - 1 >= 0 and i != n-1:
        # print("3들어옴")
        j -= 1 
        i += 1
        sum_val += 1

        arr[i][j] = sum_val
       

        
for i in range(n):
    print(*arr[i], sep = ' ')
     
    
    
# 2 2
# (0, 0) -> (0, 1) -> (1, 0) -> (0, 2) ->
# (1, 1) -> (2, 0) -> (1, 2) -> (2, 1) ->
# (2, 2)
# 3 1 
# (0, 0) -> (0, 1) -> (1, 0) -> (1, 1) ->
# (2, 0) -> (2, 1) -> (3, 0) -> (3, 1)