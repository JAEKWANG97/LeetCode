def trap( height: []) -> int:
    stack = []
    volume = 0
    max_height = 0
    i=0
    while True:
        if i == len(height):
            break
        elif max_height >= height[i]:
            volume += max_height - height[i]
        else:
            max_height = height[i] 
        i+=1
    max_height = height[i] 
    
    return volume

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))