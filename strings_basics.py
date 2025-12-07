def removeOuterParentheses(s):
    depth = 0
    res = []
    for ch in s:
        if ch == '(':
            if depth>0:
                res.append(ch)
            depth+=1

        else:
            depth-=1
            if depth>0:
                res.append(ch)
    return "".join(res)

print(removeOuterParentheses("(()())(())(()(()))"))

def largestOddNumber(num):
    for i in range(len(num)-1, -1, -1):
        if int (num[i])%2 == 1:
            return num[:i+1]
    return ""

print(largestOddNumber("52"))

def longest_commom_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    for s in strs[1:]:  # here we are comparing strings to first string which is in prefix. and in this loop we will keep shortening the prefix till we get common
        while not s.startswith(prefix):
            prefix = prefix[:-1] #here we are reducing prefix by 1 element each from end so that we get it equal to the string
            if prefix == "":
                return ""
            
    return prefix

print(longest_commom_prefix( ["flower", "flow", "flight"]))

def palindrome(s):
    i = 0
    j = len(s) - 1

    while i<j:
        while i<j and not s[i].isalnum():
            i+=1

        while i<j and not s[j].isalnum():
            j-=1

        if s[i].lower() != s[j].lower():
            return False
        
        i+=1
        j-=1
    
    return True

print(palindrome("race a car"))

def isomorphhic_strings(s,t):
    if len(s) != len(t):
        return False
    
    #we will create 2 hashamps which will map for both s2t and t2s so that mapping is done correctly from both end

    s2t = {}
    t2s = {}

    for ch_s, ch_t in zip(s,t):
        if ch_s in s2t:
            if s2t[ch_s] != ch_t:
                return False
        
        else:
            s2t[ch_s] = ch_t
        
        if ch_t in t2s:
            if t2s[ch_t] != ch_s:
                return False
        
        else:
            t2s[ch_t] = ch_s

    return True

print(isomorphhic_strings("egg", "add"))


def rotate_string(s,goal):
    if len(s) != len(goal):
        return False
        
    return goal in (s + s)

print(isomorphhic_strings("abcde", "cdeab"))

def anagram(s,t):
    return sorted(s) == sorted(t)

print(isomorphhic_strings("rat", "car"))