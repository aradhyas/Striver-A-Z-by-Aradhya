def largest_element(arr):
    n = len(arr)
    largest = arr[0]
    for i in range (n):
        if largest<arr[i]:
            largest = arr[i]
    return largest

print(largest_element([1,2,3]))

def second_largest(arr):
    '''
    Time complexity: O(n)
    '''
    large = arr[0]
    slarge = -1
    for i in range(len(arr)):
        if(arr[i]>large):
            slarge = large
            large = arr[i]
        elif(arr[i]<large and arr[i]>slarge):
            slarge = arr[i]
    return slarge

print(second_largest([8, 8, 7, 6, 5]))

def second_smallest(arr):
    '''
    Time complexity: O(n)
    '''
    import sys
    small = arr[0]
    ssmall = sys.maxsize
    for i in range(len(arr)):
        if(arr[i]<small):
            ssmall = small
            small = arr[i]
        elif(arr[i]!=small and arr[i]<ssmall):
            ssmall = arr[i]
    return ssmall

print(second_smallest([8, 8, 7, 6, 5, 1, 1]))

def check_sort(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return False
    return True

print(check_sort([1, 2, 3, 4, 5]))
print(check_sort([1, 2, 1, 6, 3]))