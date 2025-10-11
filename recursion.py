def recursion_name(n):
    if n <= 5:
        print("Aradhya")
        n = n+1
        recursion_name(n)

recursion_name(1)

print("---------------------------------------------")

def linear_num(n):
    if n <=5:
        print(n)
        n = n+1
        linear_num(n)

linear_num(1)

print("---------------------------------------------")

def backtrack_linear_num(n):
    if n<=5:
        if n<1:
            return  
        backtrack_linear_num(n-1)
        print(n)

backtrack_linear_num(4)

print("---------------------------------------------")

def reverseNumber(n):
    if n>0:
        print(n)
        n = n-1
        reverseNumber(n)

reverseNumber(5)

print("---------------------------------------------")

def backtrack_reverse_num(n):
    if n<=5:
        backtrack_reverse_num(n+1)
        print(n)

backtrack_reverse_num(1)

print("---------------------------------------------")

def sum(n):
    if n<1:
        return 0
    return n + sum(n-1)

print(sum(2))

print("---------------------------------------------")

def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

print("---------------------------------------------")

def reverse_array(n, arr):
    i = 0
    while i < n//2:
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
        i = i+1
    return arr

print(reverse_array(5, [1,2,3,4,5]))

print("---------------------------------------------")

def palindrome(i,s):
    n = len(s)
    if i>=n//2:
        return True
    if s[i]!=s[n-1-i]:
        return False
    return palindrome(i+1,s)

print(palindrome(0, "ara"))

print("---------------------------------------------")

def fibonacci(n):
    if n<=1:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))
