def pascal_triangle():
    def ncr(row, col):
        resp = 1
        r = row - 1
        c = col - 1
        c = min(c, r - c)
        for i in range(c):
            resp = resp * (r - i)
            resp = resp // (i + 1)
        return resp

    def row_of_triangle(row):
        if row <= 0:
            return []
        ans = 1
        expected_row = [1]
        for i in range(1, row):
            ans = ans * (row - i) // i
            expected_row.append(ans)
        return expected_row

    def triangle(n):
        if n <= 0:
            return []
        triangle = []
        for i in range(n):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
        return triangle

    print("Element at row 5, col 3:", ncr(5, 3))
    print("Row 5:", row_of_triangle(5))
    print("Triangle with 5 rows:")
    for r in triangle(5):
        print(r)

# Run the function
pascal_triangle()

def majority_element_II(arr):
    '''
    time - O(N), space - o(N)
    '''
    count = {}
    value = len(arr)//3
    final_list = []
    for i in arr:
        if i in count:
            count[i]+=1
        else:
            count[i] = 1

        if count[i] == value+1:
            final_list.append(i)

    return final_list

print(majority_element_II([1,2,2,3,2]))


def majorityElement_boore(nums):
        count1 = 0
        count2 = 0
        res = []
        value = len(nums)//3
        num1 = None
        num2 = None
        for x in nums:
            if x == num1:
                count1+=1
            elif x == num2:
                count2+=1
            elif count1 == 0:
                count1+=1
                num1 = x
            elif count2 == 0:
                count2+=1
                num2 = x
            else:
                count1-=1
                count2-=1
        
        count1 = count2 = 0
        for x in nums:
            if x == num1:
                count1 += 1
            elif x == num2:
                count2 += 1

        if count1>value:
            res.append(num1)
        if count2>value:
            res.append(num2)
    
        return res

print(majorityElement_boore([1,2]))

def three_sum(arr):
    n = len(arr)
    arr.sort()
    res = []
    for i in range(n-2):
        if i>0 and arr[i] == arr[i-1]:
            continue
        if arr[i] > 0:
            break
        a = arr[i]
        target = -a
        l = i+1
        r = n-1
        while l<r:
            total = arr[l]+arr[r]
            if total == target:
                res.append([arr[i],arr[l],arr[r]])
                left_val, right_val = arr[l], arr[r]
                while l < r and arr[l] == left_val:
                    l += 1
                while l < r and arr[r] == right_val:
                    r -= 1
            elif total<target:
                l+=1
            else:
                r-=1
    
    return res

print(three_sum([-1,0,1,2,-1,-4]))


def four_sum(arr,target = 0):
    n = len(arr)
    arr.sort()
    res = []
    for i in range(n-3):
        if i>0 and arr[i]==arr[i-1]:
            continue
        a = arr[i]
        for j in (i+1,n-3):
            if j>i+1 and arr[j]==arr[j-1]:
                continue
            b = arr[j]
            l = j+1
            r = n-1
            while l<r:
                total = a+b+arr[l]+arr[r]
                if total==target:
                    res.append([arr[i],arr[j],arr[l],arr[r]])
                    left_val, right_val = arr[l], arr[r]
                    while l < r and arr[l] == left_val:
                        l += 1
                    while l < r and arr[r] == right_val:
                        r -= 1
                elif total<target:
                    l+=1
                else:
                    r-=1

    return res

print(four_sum([1,0,-1,0,-2,2]))

def longest_subarray(arr):
    final_length = 0
    pref = 0
    hash_map = {0:-1}
    for i in range(len(arr)):
        pref = pref + arr[i]
        if pref in hash_map:
            final_length = max(final_length, i-hash_map[pref])
        else:
            hash_map[pref] = i
    
    return final_length

print(longest_subarray([9, -3, 3, -1, 6, -5]))

# def subarraysWithXorK(arr,k=5):
#     freq = {}
#     freq[0] = 1
#     pref = 0
#     for i in range(len(arr)):
#         pref^=i
