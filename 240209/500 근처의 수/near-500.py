arr = list(map(int, input().split()))

maxarr = []
minarr = []
for elm in arr:
    if elm < 500:
        maxarr.append(elm)
    if elm > 500:
        minarr.append(elm)
max_val = maxarr[0]
min_val = minarr[0]

for elm in maxarr:
    if elm > max_val:
        max_val = elm
for elm in minarr:
    if elm < min_val:
        min_val = elm
print(max_val, min_val)