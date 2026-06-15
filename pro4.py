#def max_arr(arr):
#    tmax = fmax= arr[0]
#    for i in range(1,len(arr)):
 #       tmax = max(arr[i], arr[i]+tmax)
  #      fmax = max(tmax, fmax)
#    return fmax

#print(max_arr([4, -2, -3, 7, -3 ]))

def spiral (arr):
    res = []
    t = l= 0
    r = len(arr[0]) -1
    b = len(arr)-1
    while l<r and t<b:
        for j in range(l, r+1):
            res.append(arr[t][j])
        t+=1
        for i in range(t, b+1):
            res.append(arr[i][r])
        r-=1
        for j in range(r,l-1, -1):
            res.append(arr[b][j])
        b-=1
        for i in range(b, t-1, -1):
            res.append(arr[i][l])
        l+=1
        if t<=b:
            for j in range(r, l-1, -1):
                res.append(arr[b][j])
        b-=1
        if l<=r:
            for i in range(b, t-1, -1):
                res.append(arr[i][l])
        l+=1
    return res
print(spiral([[2, 4, 6], [1,5,3], [8,9,10]]))