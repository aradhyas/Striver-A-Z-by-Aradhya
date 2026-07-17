class Solution:

    def subsetsWithDup(self, nums):

        nums.sort()

        ans = []
        path = []
        n = len(nums)

        def dfs(index):

            if index == n:
                ans.append(path.copy())
                return

            path.append(nums[index])
            dfs(index + 1)
            path.pop()

            while index + 1 < n and nums[index] == nums[index + 1]:
                index += 1

            dfs(index + 1)

        dfs(0)

        return ans