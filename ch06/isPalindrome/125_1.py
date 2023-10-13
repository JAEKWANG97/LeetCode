#주어진 문장열이 팰린드롬인지 확인하라. 

import sys 
import re


n =int(sys.stdin.readline().strip())

arr = list(map(int,sys.stdin.readline().strip().split(' ')))

m = int(sys.stdin.readline().strip())


for i in range(m):
    s,e = map(int, sys.stdin.readline().strip().split(' '))
    
    
def isPalindrome(input_str ) -> bool:
    input_str = re.sub(r"[^a-zA-Z0-9]", "", input_str)
    input_str = list(input_str.lower())
    left = 0
    right = len(input_str) - 1
    value = True
    while left < right:
        if input_str[left] != input_str[right]:
            value = False
            return value
        left += 1
        right -= 1
    return value

