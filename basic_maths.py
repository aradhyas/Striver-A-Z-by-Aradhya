#whenever you see a divison happening in a loop, think of log base divisor of n time complexity. Ideally we divide by 10 in case of decimal numbers. 
# but if the divisor keeps on changing, we say it is log base phi of n time complexity.


def extractionOfDigits(n):
    """Extracts the digits from a number and returns them as a list of integers.
    """
    num = 0
    while n>0:
        digit = n%10
        n=n//10
        print(digit)

print(extractionOfDigits(1234))

def countDigits(n):
    """Counts the number of digits in a positive integer.
    Time complexity: O(log base 10 of n)
    """
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count

print(countDigits(1234))

def countDigits2(n):
    """Counts the number of digits in a positive integer but using log because log base 10 of number + 1 gives number of digits.
    Time complexity: O(log base 10 of n)
    """
    import math
    from math import log10
    count = int(log10(n) + 1)
    return count

print(countDigits2(1234))

def reverseNumber(n):
    """Reverses a positive integer.
    Time complexity: O(log base 10 of n)
    """
    reverse_num = 0
    while n > 0:
        digit = n % 10
        reverse_num = reverse_num * 10 + digit
        n = n // 10
    return reverse_num

print(reverseNumber(1234))

def palindrome(n):
    """Checks if a number is a palindrome.
    Time complexity: O(log base 10 of n)
    """
    reverse_num = 0
    original_n = n  # Store the original number to compare later
    while n > 0:
        digit = n % 10
        reverse_num = reverse_num * 10 + digit
        n = n // 10

    if reverse_num == original_n:
        return True
    else:
        return False    
    
print(palindrome(12321))

def armstrong(n):
    """Checks if a number is a armstrong number.
    Time complexity: O(log base 10 of n)
    """
    sum = 0
    original_n = n  # Store the original number to compare later
    while n > 0:
        digit = n % 10
        sum = sum + digit ** 3
        n = n // 10

    if sum == original_n: 
        return True
    else:
        return False    
    
print(armstrong(371))

def divisors(n):
    """Finds all the divisors of a number.
    Time complexity: O(n)
    """
    divisors_list = []
    for i in range (1,n+1):
        if n % i == 0:
            divisors_list.append(i)
        
    return divisors_list

print(divisors(36))

def divisors2(n):
    """Finds all the divisors of a number.
    Time complexity: O(sqrt(n))
    """
    import math
    divisors_list = []
    for i in range (1,int(math.sqrt(n))+1):
        if n % i == 0:
            divisors_list.append(i)
            j = n // i
            if j != i:  # To avoid adding the square root twice if n is a perfect square
                divisors_list.append(n // i)
    divisors_list.sort()
    return divisors_list

print(divisors2(36))

def prime(n):
    """Checks if a number is prime.
    Time complexity: O((n))
    """
    count = 0
    for i in range (1,n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False

print(prime(18))


def prime2(n):
    """Finds all the divisors of a number.
    Time complexity: O(sqrt(n))
    """
    import math
    count = 0
    for i in range (1,math.isqrt(n)+1):
        if n % i == 0:
            count += 1
            j = n//i
            if j != i:    
                count += 1
    if count == 2:
        return True
    else:
        return False

print(prime2(12))

def gcd(a,b):
    """Finds the greatest common divisor of two numbers.
    Time complexity: O(min(a,b))
    """
    gcd = 1
    for i in range(1,min(a,b)+1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

print(gcd(12,15))

def gcd_euclid(a,b):
    """Finds the greatest common divisor of two numbers using Euclid's algorithm.
    Time complexity: O(log(min(a,b)))
    """
    while(a != 0 and b !=0):
        if a>b:
            a = a % b
        else:
            b = b % a
    if a == 0:
        return b
    else:
        return a    

print(gcd_euclid(12,15))

