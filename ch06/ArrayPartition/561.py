# input : 1 4 3 2
# ouput : 4

# n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.

# n은 2가 되며 최대합은 4이다.
# min(1,2) + min(3,4) = 4

# 가장 큰수.......... 큰수는 큰수끼리 작은수는 작은수끼리

# 결국은 오름차순에서 2개씩 묵는거
# 왜냐하면 다르게 작성할 경우 사용할 수 있는 큰수가 작은 수 떄문에 사용을 못함
# 큰수는 큰수끼리 페어 작은수는 작은수끼리 페어

class Solution:
    def arrayPairSum(self, nums: []) -> int:
        nums.sort()
        return sum(nums[::2])

nums = [1,4,3,2]

sol = Solution()
print(sol.arrayPairSum(nums))