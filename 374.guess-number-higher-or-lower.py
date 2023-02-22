#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        mid = (l + r) // 2
        test_mid = guess(mid)
        while test_mid != 0:
            if test_mid > 0:
                l = mid + 1
            else:
                r = mid - 1
            mid = (l + r) // 2    
            test_mid = guess(mid)
        return mid

#@lc code=end

