def two_sum_brute(arr, targetSum):
    '''
    time - O(n²), space - o(1)
    '''
    total = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == targetSum:
                return [i, j]
    return []
    
print(two_sum_brute([2,7,11,15],9))

def two_sum_map(arr, targetSum):
    '''
    time - O(n), space - o(n)
    '''
    seen = {}
    for i, x in enumerate(arr):
        left = targetSum - x
        if left in seen:
            return (seen[left], i)
        seen[x] = i

    return []
    
print(two_sum_map([3,3],6))

def sort_zero_one_two(arr):
    '''
    time - O(n), space - o(1)
    '''
    low, mid = 0,0
    high = len(arr) - 1
    while(mid<=high):
        if (arr[mid] == 0):
            arr[low], arr[mid] = arr[mid], arr[low]
            low+=1
            mid+=1
        
        elif (arr[mid] == 1):
            mid+=1
        
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high-=1
    
    return arr

print(sort_zero_one_two([2,0,2,1,1,0]))

def majority_element(arr):
    '''
    time - O(N), space - o(N)
    '''
    count = {}
    value = len(arr)//2
    for i in arr:
        if i in count:
            count[i]+=1
        else:
            count[i] = 1
        
        if count[i] > value:
            print(i)
    
    for key, value in count.items():
        print(key, value)


majority_element([3,2,3])

def majority_element_boore_method(arr):
    '''
    time - O(N), space - o(1)
    '''
    value = 0
    count = 0
    for i in range(len(arr)):
        if count == 0:
            value = arr[i]
            count+=1
        
        elif arr[i] == value:
            count+=1
        
        else:
            count-=1
    # if you want to know the count of how many times the value appeared in array
    # return arr.count(value)
    return value


print(majority_element_boore_method([2,2,1,1,1,2,2]))


def maxSubArray(total):
    '''
    time - O(N), space - o(1)
    '''
    import sys
    maxSum = 0
    start = -1
    finalStart = -1
    finalEnd = -1
    maxi = -sys.maxsize - 1
    for i in range(len(total)):
        if maxSum == 0:
            start = i
        
        maxSum+=total[i]
        if(maxSum>maxi):
            maxi = maxSum
            finalStart = start
            finalEnd = i
        
        if(maxSum<0):
            maxSum = 0
    
    print(finalStart)
    print(finalEnd)
    print(maxi)

maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

def stock_buy_sell(arr):
    '''
    time - O(N), space - o(1)
    '''
    sell = arr[0]
    maxProfit = 0
    for i in range(len(arr)):
        profit = arr[i] - sell
        maxProfit =  max(maxProfit, profit)
        sell = min(sell, arr[i])
    
    return maxProfit

print(stock_buy_sell([7,1,5,3,6,4]))

def rearrange_array(arr):
    '''
    time - O(N), space - o(N) here +ve, -ve no.s are equal
    '''
    n = len(arr)
    new_array = [0] * n
    positive = 0
    negative = 1
    for i in range(n):
        if(arr[i]<0):
            new_array[negative] = arr[i]
            negative+=2
        else:
            new_array[positive] = arr[i]
            positive+=2
    
    return new_array
print(rearrange_array([2, 4, 5, -1, -3, -4]))

def rearrange_array_different_number(arr):
    '''
    time - O(N), space - o(N) here +ve, -ve no.s are NOT equal
    '''
    n = len(arr)
    new_array = [0] * n
    positive = []
    negative = []
    for i in range(n):
        if(arr[i]<0):
            negative.append(arr[i])
        else:
            positive.append(arr[i])
    
    if(len(negative) < len(positive)):
        for i in range(len(negative)):
            new_array[2*i] = positive[i]
            new_array[(2*i) +1] = negative[i]
    
    return new_array
print(rearrange_array_different_number([3,1,-2,-5,2]))


# def next_permutation(arr):



def leader_in_array(arr):
    '''
    time - O(Nlogn), space - o(N) in worst case when every number on the right is less than the number on particular index
    '''
    import sys
    n = len(arr)
    maxi = -sys.maxsize
    ans = []
    for i in range(n-1,-1,-1):
        if arr[i]>maxi:
            ans.append(arr[i])
            maxi = arr[i]
    
    return ans

print(leader_in_array([16, 17, 4, 3, 5, 2]))

def longest_consecutive(arr):
    '''
    time - O(3N), space - o(N) time is 3N because first you add everything in set so that is O(N), then you check in while loop by 
    iterating +1 for each element so O(N) and secondly while iterating the full while loop so O(N)
    '''
    if not arr:
        return 0
    
    max_len = 0
    s = set(arr)
    for x in s:
        if x-1 not in s:
            length = 1
            curr = x
            while curr+1 in s:
                curr = curr+1
                length+=1   
            max_len = max(max_len,length)
            
    return max_len

print(longest_consecutive([100, 200, 1, 3, 2, 4]))


def matrix_zero(mat):
    '''
    Time: O(m·n), Space: O(m+n)
    '''
    if not mat or not mat[0]:
        return mat

    m, n = len(mat), len(mat[0])
    rows = [0] * m
    cols = [0] * n

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                rows[i] = 1
                cols[j] = 1

    for i in range(m):
        for j in range(n):
            if rows[i] == 1 or cols[j] == 1:
                mat[i][j] = 0

    return mat

print(matrix_zero([[1,1,1],[1,0,1],[1,1,1]]))

def matrix_zero_best(mat):
    '''
    Time: O(m·n), Space: O(1)
    '''
    if not mat or not mat[0]:
        return mat

    m, n = len(mat), len(mat[0])
    rows = [0] * m
    cols = [0] * n

    first_row = False
    for c in range(n):
        if mat[0][c] == 0:
            first_row = True
            break
    
    first_col = False
    for r in range(m):
        if mat[r][0] == 0:
            first_col = True
            break
    
    for r in range(1,m):
        for c in range(1,n):
            if mat[r][c] == 0:
                mat[r][0] = 0
                mat[0][c] = 0

    for r in range(1,m):
        for c in range(1,n):
            if mat[r][0] == 0 or mat[0][c] == 0:
                mat[r][c] = 0
    
    if first_row:
        for c in range(n):
            mat[0][c] = 0

    if first_col:
        for r in range(m):
            mat[r][0] = 0

    return mat

print(matrix_zero_best([[1,1,1],[1,0,1],[1,1,1]]))

def rotate_matrix(matrix):
    '''
    The idea is to transpose the matrix and then reverse it. Transpose makes row into column and vice versa
    Time: O(n·n), Space: O(1)
    '''
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for row in matrix:
        row.reverse()
    
    return matrix

print(rotate_matrix([[1,2,3],[4,5,6],[7,8,9]]))


def spiral_matrix(matrix):
    '''
    Time: O(n·m), Space: O(n.m)
    '''
        ans = []
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = n-1
        top = 0
        bottom = m-1

        while left <= right and top <= bottom:
            for i in range(left, right+1):
                ans.append(matrix[top][i])
            top+=1
            
            for i in range(top, bottom+1):
                ans.append(matrix[i][right])
            right-=1

            if top<=bottom:
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])
                bottom-=1

            if left<=right:
                for i in range(bottom, top-1,-1):
                    ans.append(matrix[i][left])
                left+=1

        return ans

print(spiral_matrix([[1,2,3],[4,5,6],[7,8,9]]))
