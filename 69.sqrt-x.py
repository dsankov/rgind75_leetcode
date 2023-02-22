#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def _is_root(self, test_value :int, square_value: int) -> bool:
        return (test_value ** 2 <= square_value and
                (test_value + 1) ** 2 > square_value)
        
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        
        upper = x
        bottom = 0
        test_number = (upper + bottom) // 2
        
        while not self._is_root(test_number, x):
            if test_number ** 2 > x:
                upper = test_number
            else:
                bottom = test_number
            test_number = (upper + bottom) // 2
        
        return test_number
            
        
        
# @lc code=end

