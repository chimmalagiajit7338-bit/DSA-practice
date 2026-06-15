def difference(arr):
    even_sum = 0
    odd_sum = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            even_sum = even_sum + arr[i]
        else:
            odd_sum = odd_sum + arr[i]
    return even_sum - odd_sum
numbers = [4, 6, 1, 3, 8]
print(difference(numbers))