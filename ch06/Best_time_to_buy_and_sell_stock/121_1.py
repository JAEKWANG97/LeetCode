# 한 번의 거래로 낼 수 있는 최대 이익을 산출하라

# 1일 떄 사서 6일 때 팔면 이익을 얻는다. 

import sys
prices = [7,6,4,3,1]

# 브르투 포스

def brute_force(prices):
    max_stock = 0
    for buy in range(len(prices)):
        for sell in range(buy , len(prices)):
            max_stock = max(max_stock, prices[sell] - prices[buy])
    return (max_stock)

def point_max(prices):
    max_stock = 0
    for i in range(len(prices)):
        max_stock = max(max_stock ,  max(prices[i:])-prices[i])
    
    return (max_stock)
def get_max_profit(prices):
    min_price = sys.maxsize
    max_prorfit = 0
    for x in prices:
        max_prorfit = max(max_prorfit ,  x-min_price )
        if min_price > x:
            min_price = x
        
    return max_prorfit

print(get_max_profit(prices))