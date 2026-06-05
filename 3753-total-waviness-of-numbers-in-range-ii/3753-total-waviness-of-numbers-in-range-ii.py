from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(x):
            if x <= 0:
                return 0

            digits = list(map(int, str(x)))
            n = len(digits)

            @lru_cache(None)
            def dp(pos, prev2, prev1, started, tight):
                if pos == n:
                    return (1, 0)  # count of numbers, total waviness

                limit = digits[pos] if tight else 9

                total_count = 0
                total_wavy = 0

                for d in range(limit + 1):
                    new_tight = tight and (d == limit)

                    if not started and d == 0:
                        count, wavy = dp(pos + 1, -1, -1, False, new_tight)
                        total_count += count
                        total_wavy += wavy
                    else:
                        add = 0

                        if started and prev2 != -1:
                            if (prev1 > prev2 and prev1 > d) or (prev1 < prev2 and prev1 < d):
                                add = 1

                        count, wavy = dp(pos + 1, prev1, d, True, new_tight)

                        total_count += count
                        total_wavy += wavy + add * count

                return (total_count, total_wavy)

            return dp(0, -1, -1, False, True)[1]

        return solve(num2) - solve(num1 - 1)