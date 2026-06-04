class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        wavy = 0
        for i in range(num1,num2+1):
            s = str(i)
            for j in range(1,len(s)-1):
                left = s[j-1]
                mid = s[j]
                right = s[j+1]
                if mid > left and mid > right or mid < left and mid < right:
                    wavy+=1

        return wavy 