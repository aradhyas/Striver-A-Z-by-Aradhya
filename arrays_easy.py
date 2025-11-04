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


def remove_duplicates(arr):
    '''
    Time complexity: O(n), Space O(1). Here we are counting the number of duplicates in a sorted array and returning the count
    '''
    i = 0
    for j in range(1,len(arr)):
        if(arr[i]!=arr[j]):
            arr[i+1] = arr[j]
            i+=1
    return i+1

print(remove_duplicates([1, 1, 2, 2, 3, 3]))

def left_rotate(arr,d):
    '''
    Time complexity: O(n), Space O(n). This is the brute force solution for left rotating the array
    '''
    n = len(arr)
    d%=n
    if d==0:
        return arr
    temp = arr[:d]
    for i in range(d,n):
        arr[i-d] = arr[i]
    arr[n-d:] = temp
    # for i in range(n-d,n):
    #     arr[n-d] = temp[i-(n-d)]
    return arr

print(left_rotate([1,2,3], 1))

def reverse(arr,left,right):
    while left<right:
        arr[left], arr[right] = arr[right], arr[left]
        left+=1
        right-=1

def left_rotate_reverse(arr,d):
    '''
    Time complexity: O(2n), Space O(1). This is the brute force solution for left rotating the array
    '''
    n = len(arr)
    d%=n
    if d==0:
        return arr
    
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr, 0, n-1)

    return arr

print(left_rotate_reverse([1,2,3], 9))

def move_zeroes(arr):
    '''
    Time complexity: O(n), Space O(1)
    '''
    n = len(arr)
    insert = 0
    for x in arr:
        if x!=0:
            arr[insert] = x
            insert+=1
        
    for i in range(insert, n):
        arr[i] = 0
    return arr

print(move_zeroes([1,0,2,0,3]))

def move_zeroes_second_method(arr):
    '''
    Time complexity: O(n), Space O(1)
    '''
    j = -1
    for i in range(len(arr)):
        if arr[i] == 0:
            j = i
            break
    
    if(j==-1): return arr

    for i in range(j+1, len(arr)):
        if arr[i]!=0:
            arr[i], arr[j] = arr[j],arr[i]
            j+=1
    
    return arr

print(move_zeroes_second_method([1,0,2,0,3]))

def linear_search(arr,x):
    index = []
    for i in range(len(arr)):
        if x == arr[i]:
            index.append(i)
    return index

print(linear_search([1,0,2,0,3], 0))

def union_two_arrays(arr1, arr2):
    m, n = len(arr1), len(arr2)
    union_array = []
    i = j = 0

    while i < m and j < n:
        if arr1[i] == arr2[j]:
            union_array.append(arr1[i]) 
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            union_array.append(arr1[i])
            i += 1
        else:
            union_array.append(arr2[j])
            j += 1

    while i < m:
        union_array.append(arr1[i])
        i += 1
    while j < n:
        union_array.append(arr2[j])
        j += 1

    return union_array

print(union_two_arrays([1,2], [1,3,4]))


def intersect_two_arrays(arr1, arr2):
    m, n = len(arr1), len(arr2)
    intersect_array = []
    seen_array = [0] * n
    i = j = 0

    for i in range(m):
        for j in range(n):
            if arr1[i] == arr2[j] and seen_array[j] == 0:
                intersect_array.append(arr1[i])
                seen_array[j] = 1
                break

    return intersect_array

print(intersect_two_arrays([1,2,2,1], [2,2]))

def intersect_two_arrays_second(arr1, arr2):
    '''
    Time: O(m + n)
    Space: O(1)
    '''
    arr1.sort()
    arr2.sort()
    m, n = len(arr1), len(arr2)
    intersect_array = []
    i,j = 0,0
    while i<m and j<n:
        if(arr1[i]<arr2[j]):
            i+=1
        elif(arr1[i]>arr2[j]):
            j+=1
        else:
            if not intersect_array or intersect_array[-1] != arr1[i]:
                intersect_array.append(arr1[i])
            i+=1
            j+=1

    return intersect_array

print(intersect_two_arrays_second([1,2,2,1], [2,2]))

def find_missing_number(arr,n):
    '''
    Time: O(n)
    Space: O(1)
    '''
    arr_sum = n*(n+1)/2
    total = 0
    for i in arr:
        total+=i
    
    missing_num = arr_sum - total
    return int(missing_num)

print(find_missing_number([1,3],3))

def find_missing_number_using_XOR(arr,n):
    '''
    Time: O(n)
    Space: O(1)
    both the logics have same complexitites but XOR works better in situations when size of array is really big like 10^5
    '''
    xor1 = 0
    xor2 = 0
    m = n-1
    for i in range(0,m):
        xor1^=arr[i]
        xor2^=(i+1)
    xor2 ^= n 
    missing_num = xor2^xor1
    return int(missing_num)

print(find_missing_number_using_XOR([1,3],3))

def find_max_1s(arr):
    count = 0
    maxi = 0
    for i in arr:
        if i==1:
            count+=1
            maxi = max(count,maxi)
        
        else:
            count = 0
    
    return maxi

print(find_max_1s([1,1,0,1,1,1,0]))

def num_appears_once(arr):
    '''
    Time: O(n)
    Space: O(1)
    so map takes O(nlog(map size)) and xor takes less time than that
    '''
    xorr = 0
    for i in range(len(arr)):
        xorr = xorr ^ arr[i]
    return xorr

print(num_appears_once([1,1,2,3,3,4,4]))

def subarraySum(arr,k):
    max_length = 0
    for i in range(len(arr)):
        total = 0
        for j in range(len(arr)):
            total+=arr[j]
            if total == k:
                max_length = max(max_length, j - i + 1)
    
    return max_length

print(subarraySum([2, 3, 5, 1, 9],10))