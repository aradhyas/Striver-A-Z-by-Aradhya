def selection_sort(arr):
    "Time complexity: O(n^2)"
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if arr[j] < arr[min]:
                min = j 
        arr[i], arr[min] = arr[min], arr[i]
    return arr

print(selection_sort([64, 25, 12, 22, 11]))

def bubble_sort(arr):
    "Time complexity: O(n^2)"
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

print(bubble_sort([64, 25, 12, 22, 11]))

def insertion_sort(arr):
    "Time complexity: O(n^2)"
    n = len(arr)
    for i in range(n):
        j = i
        while(j>0 and arr[j-1]>arr[j]):
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -=1
    return arr

print(insertion_sort([64, 25, 12, 22, 11]))

def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid+1
    while(left<=mid and right<=high):
        if(arr[left]<=arr[right]):
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1

    while(left<=mid):
        temp.append(arr[left])
        left+=1
    while(right<=high):
        temp.append(arr[right])
        right+=1
    arr[low:high+1] = temp

def merge_sort(arr, low, high):
    # Time complexity: O(n*logn), space(O(n))
    if low >= high:      
        return
    mid = (low+high)//2
    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    merge(arr,low,mid,high)


a = [5, 2, 4, 6, 1, 3]
merge_sort(a, 0, len(a) - 1)
print(a) 

def quick_function(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quick_sort(arr, low, high):
    if low<high:
        partition = quick_function(arr,low,high)
        quick_sort(arr,low, partition-1)
        quick_sort(arr, partition+1, high)

a = [5, 2, 4, 6, 1, 3]
quick_sort(a, 0, len(a) - 1)
print(a) 

