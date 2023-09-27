def min_cost_stairs(cost):
    n = len(cost)
    
    if n == 0: return 0
    if n == 1: return cost[0]
    
    # 각 계단까지의 최소 비용을 저장할 배열 초기화
    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]
    
    # 2번째 계단부터 최소 비용 계산
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    
    # 인덱스 0 또는 인덱스 1에서 시작할 수 있기 때문에, 마지막 계단 또는 그 이전 계단의 최소 비용 중에서 가장 작은 값을 반환
    return dp[n-1]

cost = [10, 15, 20]
print(min_cost_stairs(cost))  # 예상 출력값: 15