#계단 오르기
# 1계단 2계단씩 오를 수 있음
# n계단 까지 가는데 경우의 수는?

def climb_stairs(n : int):
    if n == 1:
        return 1
    if n == 2:
        return 2
    n = climb_stairs(n-1) + climb_stairs(n-2)
    return n

print(climb_stairs(3))

n = 7

memo = [0] * (n+1)

def climbStairs_memo(n , memo : []):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    memo[n] = climbStairs_memo(n-1 , memo) + climbStairs_memo(n-2 , memo)
    return memo[n]

print(climbStairs_memo(7 , memo))

memo = [0] * (n+1)

def climbStairs_bottom_up(n , memo : []):
    
    memo[1], memo[2] = 1, 2

    
    for i in range(3 , n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]

    