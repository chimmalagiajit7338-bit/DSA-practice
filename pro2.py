#def bss(arr):
# #   l=len(arr)
#    max=0
#    for i in range(l):   #1 2 3
#        for j in range(i+1, l):  #1, 2, 3
 #           if (arr[j] -arr[i]>max):
#                max = arr[j]-arr[i]
#    return max
#print(bss([6,7,1,2,8,5,9]))
#print(bss([6,7,1,2,8,5,9]))



###
def bss_eff(arr):
    buy = arr[0]
    res = 0
    for i in range(1, len(arr)):
        buy = min(buy, arr[i])
        res = max(res, arr[i]-buy)
    return res
print(bss_eff([5,4,1,3,8,9]))

def prod_itself(arr):
    n=len(arr)
    p=1
    for i in range(n):
        p*=arr[i]
    res = [1]*n
    for i in range(n):
        res[i]=p//arr[i]
    return res
print(prod_itself([7,5,2,1]))


