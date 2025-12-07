def binary_search(arr, target):
    """
    TC - O(log n base2)
    """
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = int((low+high)/2)
        if arr[mid] == target:
            return mid
        elif target>arr[mid]:
            low = mid+1
        else:
            high = mid-1
    
    return -1

print(binary_search([-1,0,3,5,9,12],9))


def binary_search_recursive(arr,low,high,target):
    if low>high:
        return -1
    mid = int((low+high)/2)
    if arr[mid] == target:
        return mid
    elif arr[mid]<target:
        return binary_search_recursive(arr,mid+1,high,target)
    else:
        return binary_search_recursive(arr,low,mid-1,target)
    
def search(arr, target):
    return binary_search_recursive(arr,0,len(arr)-1,target)

print(search([-1,0,3,5,9,12],9))

def lower_bound(arr, target):
    """
    TC - O(log n base2)
    """
    low = 0
    high = len(arr)-1
    ans = len(arr)
    while low<=high:
        mid = int((low+high)/2)
        if arr[mid]>=target:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans

print(lower_bound([3,5,8,15,19],9))

def upper_bound(arr, target):
    """
    TC - O(log n base2)
    """
    low = 0
    high = len(arr)-1
    ans = len(arr)
    while low<=high:
        mid = int((low+high)/2)
        if arr[mid]>target:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans

print(upper_bound([3,5,8,9,15,19],9))

def first_last_occurence(arr,target):
    """
    TC -2* O(log n base2) SC - O(1)
    So basically for this you can get first occurence in lower bound because first occurence would be <=target
    And (upper bound - 1) would be the last occurence because upper bound>target so 1 less than that position would give last occurence
    The edge case that would be covered would be that target should definitely be in the array and its lower/upper bound should not get an index out of the array

    And if you want to get count of total occurence = first-last+1
    """
    n = len(arr)
    first = lower_bound(arr, target)

    if (first==n or arr[first]!=target):
        return {-1,-1}
    else:
        return {first, (upper_bound(arr, target) - 1)}

print(first_last_occurence([3,4,13,13,13,20,40],13))

def first_occurence(arr,target):
    """
    TC - O(log n base2)
    If lower bound/upper bound is not allowed
    """
    first = -1
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == target:
            first = mid
            high = mid-1
        
        elif arr[mid]<target:
            low = mid+1
        
        else:
            high = mid-1
    
    return first

print(first_occurence([3,4,13,13,13,20,40],13))

def last_occurence(arr,target):
    """
    TC - O(log n base2)
    If lower bound/upper bound is not allowed
    """
    last = -1
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == target:
            last = mid
            low = mid+1
        
        elif arr[mid]<target:
            low = mid+1
        
        else:
            high = mid-1
    
    return last

print(last_occurence([3,4,13,13,13,20,40],11))

def search_rotated(arr,target):
    """
    TC - O(log n base2)
    """
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        
        elif arr[low]<arr[mid]:
            if arr[low] <= target and target<arr[mid]:
                high = mid-1
            else:
                low = mid+1

        else:
            if arr[high] <= target and target>=arr[mid]:
                low = mid+1
            else:
                high = mid-1

    return -1

print(search_rotated([4,5,6,7,0,1,2,3],0))

def search_rotated_II(arr,target):
    """
    TC - O(log n base2)
    """
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            low+=1
            high-=1
        
        elif arr[low]<arr[mid]:
            if arr[low] <= target and target<arr[mid]:
                high = mid-1
            else:
                low = mid+1

        else:
            if arr[high] <= target and target>=arr[mid]:
                low = mid+1
            else:
                high = mid-1

    return -1

print(search_rotated_II([7, 8, 1, 2, 3, 3, 3, 4, 5, 6],3))

def minimum_rotated_array(arr):
    """
    TC - O(log n base2)
    This code also contains the number of times the array has been rotated which we can get to know with the index of minimum number in the array
    """
    import sys
    ans = sys.maxsize
    index = -1
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[low]<arr[mid]:
            ans = min(ans,arr[low])
            index = low
            low = mid+1

        else:
            high = mid-1
            index = mid
            ans = min(ans,arr[mid])
    
    return ans

print(minimum_rotated_array([7, 8, 3, 3, 3, 4, 5, 6]))

def single_element(arr):
    n = len(arr)
    if n==1:
        return arr[0]
    if(arr[0]!=arr[1]):
        return arr[0]
    if(arr[n-1]!=arr[n-2]):
        return arr[n-1]
    low = 1
    high = n-2
    while(low<=high):
        mid = (low+high)//2

        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
            return arr[mid]
        if arr[mid] == arr[mid-1] and mid%2!=0 or arr[mid] == arr[mid+1] and mid%2==0:
            low = mid+1
        else:
            high = mid-1

    return -1

print(single_element([1,1,2,2,3,3,4,5,5,6,6]))


def peak_element(arr):
    n = len(arr)
    low = 1
    high = n-2
    if len(arr) == 1:
        return arr[0]
    
    if arr[0]>arr[1]:
        return arr[0]
    
    if arr[n-1]>arr[n-2]:
        return arr[n-1]
    
    while low<=high:
        mid = (low+high)//2
        if arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]:
            return arr[mid]
        
        elif arr[mid]>arr[mid-1]:
            low = mid+1

        else:
            high = mid-1
    
    return -1

    
print(peak_element([1,2,1,3,5,6,4]))