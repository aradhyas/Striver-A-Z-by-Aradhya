def lower_bound(arr,num):
    ans = len(arr)
    low = 0
    high = len(arr)-1
    while (low<=high):
        mid = (low+high)//2
        if arr[mid]>=num:
            ans = mid
            high = mid-1

        else:
            low = mid+1
    
    return ans


def max_ones(mat,m):
    """
    consider every row as an array and check lower bound for each
    """
    count_max = 0
    index = -1
    for r, row in enumerate(mat):
        first_one_idx = lower_bound(row, 1)
        count_ones = m - first_one_idx   # if no 1s, this becomes 0
        if count_ones > count_max:
            count_max = count_ones
            index = r

    return index if count_max > 0 else -1   

mat = [
    [1, 1, 1],
    [0, 0, 1],
    [0, 0, 0]
]
m = 3

print(max_ones(mat, m))  