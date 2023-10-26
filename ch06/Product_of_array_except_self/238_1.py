#자신을 제외한배열의 곱

nums = [1,2,3,4]

in_ordered_multi =[]
reversed_multi = []

temp = 1
for i in range(len(nums)):
    in_ordered_multi.append(temp)
    temp *= nums[i]

temp = 1    
for i in range(len(nums) - 1, 0 - 1 , -1):
    reversed_multi.append(temp)
    temp *= nums[i]
    
reversed_multi.reverse()

answer = []
for i in range(len(nums)):
    left = in_ordered_multi[i]
    right = reversed_multi[i]
    answer.append(left * right)

print(answer)