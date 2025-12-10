def sort_by_freq(s):
    """
    Idea is to create hashmap, then add it in a list with freq first and then character tuple (freq,ch)
    then sort in desc and then run a loop to print the final string
    time - O(nlogn)
    space - O(n)
    """
    hash_len = {}
    pair = []
    res = []
    for ch in s:
        if ch in hash_len:
            hash_len[ch]+=1
        else:
            hash_len[ch]=1

    for ch, freq in hash_len.items():
        pair.append((freq,ch))

    pair.sort(reverse=True)

    for freq,ch in pair:
        res.append(freq*ch)

    return "".join(res)

print(sort_by_freq("tree"))

def max_depth(s):
    depth = 0
    max_depth = 0
    for ch in s:
        if ch=='(':
            depth+=1
            max_depth=max(depth,max_depth)
        if ch==')':
            depth-=1
    
    return max_depth

print(max_depth("(1)+((2))+(((3)))"))
        

def romanToInt(s):
        values = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
            }

        n = len(s)
        total = 0

        for i in range(n-1):
            curr = values[s[i]]
            nxt = values[s[i+1]]
            if curr<nxt:
                total-=curr
            else:
                total+=curr
        
        total+=values[s[-1]]

        return total

print(romanToInt("MCMXCIV"))

def implement_atoi(s):
    s = s.strip() #this is to remove any whitespaces
    sign = 1
    i = 0
    num = 0
    if not s:
        return 0
    first_ch = s[0]
    if first_ch == '-':
        sign = -1
        i+=1
    if first_ch == '+':
        sign = 1
        i+=1

    while i <len(s) and s[i].isdigit(): # this is to check after the sign(+/-) whether the string has a num or not
        digit = int(s[i])
        num = num*10 + digit
        i+=1
    
    num = num*sign
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1

    if num < INT_MIN:
        return INT_MIN
    if num > INT_MAX:
        return INT_MAX
    return num

print(implement_atoi("1337c0d3"))

def reverse_words(s):
    """
    The idea is to split str into a list because we want to reverse words and not each character
    Then 2 pointer approach where we will swap and increase/decrease the pointer
    Time - O(n) for split because it will go through entire str. then you put it in words which can be <=n
    Space - O(n) because words are taking up space and then you build a new string in result
    """
    words = s.split()
    left = 0
    right = len(words) - 1
    while left<right:
        words[left], words[right] =  words[right],words[left]
        left+=1
        right -=1
    
    result = " ".join(words)
    return result

print(reverse_words("a good   example"))