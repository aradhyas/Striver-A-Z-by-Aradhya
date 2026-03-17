class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                result[prev] = i - prev

            stack.append(i)     
        return result

# dry run
# stack = [0]
# prev = 0
# res[0] = 1-0

# stack = [1]
# prev = 1
# res[1] = 2-1

# stack =[2,3,4]
# prev = 4
# res[4] = 5-4
# prev = 3
# res[3] = 5-3 =2

# stack = 2,5

# prev = 5
# res[5] = 6-5 = 1
# res[2] = 6-2 = 4

# stack = [6]
