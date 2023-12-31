nums = [0,3,3]
target = 6

output = [0,1]
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 하나의 for문으로 통합
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target-num] , i]
            nums_map[num] = i
        pass

sol  = Solution()

print(sol.twoSum(nums, target))