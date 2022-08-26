arr = list(range(1,10))

def binary(arr, x):
    l = 0
    r = len(arr)-1
    while l < r:
        mid = l + (r-l)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            r = mid
        else:
            l = mid + 1
    return l

print(arr)
print(binary(arr, 5))
print(binary(arr, 5.5))
print(binary(arr, 4.5))
