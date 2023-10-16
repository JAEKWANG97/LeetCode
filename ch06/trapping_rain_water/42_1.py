# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라

from typing import List


height = [0,1,0,2,1,0,1,3,2,1,2,1]
output  = 6

class Solution:
    def trap(self, height: List[int]) -> int:
        # left , right 각각의 max를 뽑으면서 진행
        # max 보다 현재 높이가 낮으면 volume 계산
        volume = 0
        left = 0
        right = len(height) -1
        # 최댓값으로 하면 안되나 했는데 되긴 될듯
        max_height = max(height)
        standard = height.index(max_height)
        # 왼쪽 따로 오른쪽 따로
        # 처음에 max와 현재 높이를 비교 후 max 최신화
        # 그 다음에는 max와 현재높이의 차를 volume에 ++ 
        # max가 0 이여도 무방. 로직상 0 - 0 을 볼륨에 추가될 것
        
        max_left = height[left]
        max_right = height[right]
        print(standard)
        while left <= standard:
            max_left = max(max_left , height[left])
            volume += (max_left - height[left])
            left+= 1
      

        while right >= standard:
            max_right = max(max_right , height[right])
            volume += (max_right - height[right])
            right-=1
   
        return volume
            
sol = Solution()
arr = sol.trap(height)
print(arr)