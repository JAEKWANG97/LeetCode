height = [4,2,0,3,2,5]
output  = 6

max_height = max(height)
max_height_index = height.index(max_height)

# 좌우 기준 가장 큰 높이까지의 이동을 본다.

# 좌우 포인터 생성
left = 0
right = len(height) - 1

max_left = 0
max_right = 0


volume = 0

while left < max_height_index:
    if max_left <= height[left]:
        max_left = height[left]
    volume += max_left - height[left]
    left += 1

while right > max_height_index:
    if max_right <= height[right]:
        max_right = height[right]
    volume += max_right - height[right]
    right -= 1
        
print(volume)