# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

import collections

s = "cccc"

def dp_table(s : str):
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
    max_length = 0
    max_strs = ''
    # 문자열이 하나인 경우
    for i in range (len(s)):
        dp[i][i] = 1
        max_length = 1
        max_strs = ''.join(s[i])
    
    # 문자열이 두개인 경우
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            dp[i][i+1] = 2
            max_length = 2
            max_strs = ''.join(s[i:i+2])
            
    
    for length in range(3,len(s)+1):
        for i in range(len(s) - length + 1):
            j = length + i - 1
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = length
                if max_length < length:
                    max_strs = ''.join(s[i:j+1])                   
                    
    return max_strs

print(dp_table(s))