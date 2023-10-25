# 배열 파티션
# n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가자아 큰 수를 출력하라

nums = [1,4,3,2]
# 출력 => 4

nums.sort()
sum = 0
for i in range(len(nums)):
    if i % 2 == 0:
        sum += nums[i]

print(sum)