def sqrt_bs(num):
    low = 0
    high = num
    sqrt = 0
    while low<=high:
        mid = (low+high)//2
        if (mid*mid <= num):
            low = mid+1
            sqrt = mid
        else:
            high = mid-1
    
    return sqrt

print(sqrt_bs(128))

def nth_root(n, m) -> int:
    if m in (0, 1):
        return m

    low, high = 1, m
    while low <= high:
        mid = (low + high) // 2
        val = mid ** n

        if val == m:
            return mid
        if val < m:
            low = mid + 1
        else:
            high = mid - 1

    return -1


print(nth_root(3,27))

def find_max(arr):
    import sys
    maxi = sys.maxsize
    for i in arr:
        maxi = max(i,maxi)
    return maxi

def calculate_hours(arr,h):
    import math
    n = len(arr)
    total_hours = 0
    for i in arr:
        total_hours+= math.ceil(i/h)
    return total_hours

def koko_bananas(arr,h):
    low = 1
    high = find_max(arr)
    total_hours = 0
    while low <= high:
        mid = (low + high) // 2
        total_hours = calculate_hours(arr,mid)
        if total_hours<=h:
            high = mid-1
        else:
            low = mid+1
    return low

print(koko_bananas([7, 15, 6, 3],8))

def divisor_sum(arr,limit):
    import math
    sum = 0
    for i in arr:
        sum+= math.ceil(i/limit)
    return sum

def smallest_divisor(arr,limit):
    low = 1
    high = find_max(arr)
    while low<=high:
        mid = (low + high) // 2
        if (divisor_sum(arr,mid)<=limit):
            high = mid-1
        else:
            low = mid+1
    return low

print(smallest_divisor([44,22,33,11,1],5))


def bouquets_possible(arr,day,bouquets,flowers):
    count = 0
    total_bouquets = 0
    for i in arr:
        if i<=day:
            count+=1
            if count==flowers:
                bouquets+=1
                count=0
            else:
                count=0
    return total_bouquets>=bouquets

def min_days_to_make_bouquets(arr,bouquets,flowers):
    import sys
    high = -sys.maxsize
    low = sys.maxsize
    for i in arr:
        high = max(i,high)
    for i in arr:
        low = min(i,low)
    if (bouquets * flowers) > len(arr):
        return -1
    
    while(low<=high):
        mid = (low+high)//2
        if(bouquets_possible(arr,mid,bouquets,flowers)):
            high = mid-1
        else:
            low = mid+1    
    return low

    
print(min_days_to_make_bouquets([1,10,2,9,3,8,4,7,5,6],4,2))


def smallest_divisor_sum(arr,threshold):
    import math
    sum = 0
    for i in arr:
        sum+= math.ceil(i/threshold)
    return sum

def smallest_divisor_threshold(arr,threshold):
    import sys
    high = -sys.maxsize
    low = sys.maxsize
    for i in arr:
        high = max(i,high)
    for i in arr:
        low = min(i,low)
    
    while low<=high:
        mid = (low+high)//2
        if (smallest_divisor_sum(arr,mid)<=threshold):
            high = mid-1
        
        else:
            low = mid+1
    
    return low

print(smallest_divisor_threshold([1,2,5,9],7))


