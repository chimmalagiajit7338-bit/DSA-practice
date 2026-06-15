#arr = [34,56,78,12,34]
#print(arr)
#print(arr[3])

#


# Rat count house
# []

def count_rat(r, u, arr):
    if(len(arr) ==0):
        return  -1
    
    freq = r*u
    bag = 0

    for i in range(len(arr)):
        bag += arr[i] # 0+2=2, 2+3=5  5+1=6 6+4 = 10
        if bag >= freq:
            return i+1
    return 0
                 
            
   
print(count_rat(4,2,[2,3,1,4,5,6]))

    